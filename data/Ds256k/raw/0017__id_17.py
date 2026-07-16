# Auto-extracted from ds_lt256k_500.jsonl
# record_id=17  entry=f  input='15'  output='230'  tokens=136294

def f(x):
    t0 = (x & 12) << 3
    aux = t0 * 4
    t1 = 4 * x & x
    nxt = t1 - (3 + 8 | x)
    cur = x | nxt
    for e in range(338):
        aux = ((cur << 4) - aux) % 65521
        cur = (x * x - cur) % 97
        t2 = 5 + x
        t3 = t2 | e & nxt
        cur = cur >> 1 & t3
    buf = cur + cur + (x & 13)
    return (8 - x + aux) % 251

if __name__ == "__main__":
    arg = 15
    expected = 230
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
