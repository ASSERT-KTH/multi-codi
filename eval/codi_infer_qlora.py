"""CODI inference for a QLoRA adapter checkpoint (train/train_codi_qlora.py output:
adapter_config.json + adapter_model.safetensors + thought_projector.pt, no full model
weights). Separate from codi_infer.py because the QLoRA path needs a base_model +
adapter_dir split (the adapter dir alone has no tokenizer/config) and reuses CWM's
native <|reasoning_thinking_start/end|> tokens as latent markers instead of the
add_trace_tokens()-injected <|latent_start/end|> used by non-CWM bases -- CWM's
tokenizer already has the trace-format tokens natively, and LoRA never trains new
embeddings, so nothing gets added/resized here (mirrors train_codi_qlora.py exactly).

gen_latent/gen_single are unchanged and imported from codi_infer.py: they only touch
model.model/model.prj/model._latent_block/model.latent_steps, an interface this
module's CodiQloraModel implements the same way.
"""

import os

import torch
from peft import PeftModel
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from train.codi_core import build_projector, sliding_window

LATENT_START = "<|reasoning_thinking_start|>"
LATENT_END = "<|reasoning_thinking_end|>"

# ids consumed by eval_len.py's MODE=codi path; kept in the same shape as
# data.tokens.token_ids() so the caller's code doesn't need to branch.
_NEEDED = ["<|line_sep|>", "<|action_sep|>", "<|end_of_text|>"]


class CodiQloraModel(torch.nn.Module):
    """Eval-time counterpart of train.train_codi_qlora.CodiModel. That class rebuilds
    a chunked KV cache per call so training's checkpoint/backward recompute stays
    cheap; eval never does backward, so this uses a plain incrementally-extended
    past_key_values cache instead (same latent-block math, matches gen_latent's
    step()/`_latent_block` interface from codi_infer.py)."""

    def __init__(self, peft_model, prj, latent_start_id, latent_end_id, latent_steps):
        super().__init__()
        self.model = peft_model
        self.prj = prj
        self.latent_steps = latent_steps
        dev = next(peft_model.parameters()).device
        self._ls_tok = torch.tensor([[latent_start_id]], device=dev)
        self._le_tok = torch.tensor([[latent_end_id]], device=dev)

    def _emb(self, ids):
        return self.model.get_input_embeddings()(ids)

    @torch.no_grad()
    def _latent_block(self, cache):
        o = self.model(inputs_embeds=self._emb(self._ls_tok), past_key_values=cache,
                       use_cache=True, output_hidden_states=True)
        cache, h = o.past_key_values, o.hidden_states[-1][:, -1:]
        for _ in range(self.latent_steps):
            o = self.model(inputs_embeds=self.prj(h), past_key_values=cache,
                           use_cache=True, output_hidden_states=True)
            cache, h = o.past_key_values, o.hidden_states[-1][:, -1:]
        o = self.model(inputs_embeds=self._emb(self._le_tok), past_key_values=cache, use_cache=True)
        return o.past_key_values, o.logits[:, -1]


def load_codi_qlora(base_model, adapter_dir, latent_steps, dev, sw=0,
                    attn_impl="flash_attention_2", load_in_4bit=True):
    """base_model: HF dir for tokenizer/config (e.g. model_weights/cwm_hf).
    adapter_dir: a checkpoint-N dir from train_codi_qlora.py (adapter + projector).
    load_in_4bit: match training precision (QLoRA base was frozen 4-bit nf4)."""
    tok = AutoTokenizer.from_pretrained(base_model, use_fast=True)
    ids = {t: tok.convert_tokens_to_ids(t) for t in _NEEDED}
    cfg = sliding_window(AutoConfig.from_pretrained(base_model), sw)

    load_kwargs = dict(config=cfg, torch_dtype=torch.bfloat16, attn_implementation=attn_impl)
    if load_in_4bit:
        load_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16)
        load_kwargs["device_map"] = {"": dev}
    base = AutoModelForCausalLM.from_pretrained(base_model, **load_kwargs)
    if not load_in_4bit:
        base = base.to(dev)

    peft_model = PeftModel.from_pretrained(base, adapter_dir).eval()
    prj = build_projector(base.config.hidden_size, next(base.parameters()).device, torch.bfloat16)
    prj.load_state_dict(torch.load(os.path.join(adapter_dir, "thought_projector.pt"), map_location="cpu"))

    latent_start_id = tok.convert_tokens_to_ids(LATENT_START)
    latent_end_id = tok.convert_tokens_to_ids(LATENT_END)
    assert tok.unk_token_id in (None, -1) or latent_start_id != tok.unk_token_id, \
        f"{LATENT_START!r} not in base tokenizer vocab"
    model = CodiQloraModel(peft_model, prj, latent_start_id, latent_end_id, latent_steps)
    return tok, ids, model
