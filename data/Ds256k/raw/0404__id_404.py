# Auto-extracted from ds_lt256k_500.jsonl
# record_id=404  entry=f  input='14'  output='2835'  tokens=177608

def f(x):
    t0 = x & 20 | x
    c = t0 * (x * x ^ x)
    nxt = c * x * c % 1009
    if x << 1 != 21:
        x = 16 * x
        nxt = nxt - 7
    p = x ^ c
    t1 = x & c
    tot = t1 * (x & p)
    buf = 0
    while buf < 423:
        if p // 8 > 37:
            t2 = nxt ^ 19
            t3 = t2 - tot * p
            nxt = t3 % 1009
            t4 = tot ^ 8 ^ buf
            nxt = t4 % 1009
        p = ((10 - tot) // 5 | buf) % 4093
        buf = buf + 1
    return ((c | 8) + 7) % 4093

if __name__ == "__main__":
    arg = 14
    expected = 2835
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
