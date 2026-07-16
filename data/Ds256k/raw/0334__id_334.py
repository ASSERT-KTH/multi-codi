# Auto-extracted from ds_lt256k_500.jsonl
# record_id=334  entry=f  input='2'  output='16312'  tokens=255618

def f(x):
    for z in range(12):
        t0 = (19 ^ 9) * z
        x = (t0 - x) % 17
    res = x * x - x
    tot = res * x
    a = tot & res
    t1 = (a >> 2) - x
    t2 = t1 * (a - 11 + tot)
    buf = t2 & 262143
    acc = tot & x
    e = 0
    while e < 8:
        t3 = 19 * buf - (tot - 12)
        x = (t3 - (1 - buf - x)) % 17
        e = e + 1
    prv = a % 97
    for cnt in range(65):
        for w in range(5):
            buf = (prv // 5 | w) % 9973
            t4 = cnt * acc
            t5 = t4 * (tot >> 2)
            prv = (t5 | w) % 17
        if 10 - 16 - x < 19:
            t6 = (17 - 4) * 2
            tot = (t6 - tot) % 65521
            t7 = x + tot >> 2
            x = t7 % 97
    nxt = 19 + 10 ^ prv
    v = res
    lo = tot + a + prv
    if prv & nxt == 39:
        lo = 11 * x & 3
        v = x + 18 + acc
    else:
        buf = lo >> 2 & nxt
    val = acc + tot
    tmp = 16 * x
    q = (x | acc) + val
    if tmp | 20 <= 32:
        a = x - a
        t8 = val - q + tmp * a
        lo = (t8 ^ prv) & 131071
    else:
        acc = 7 + a | prv
    d = 20 << 1 | val
    return ((10 | v) >> 1 ^ lo) & 16383

if __name__ == "__main__":
    arg = 2
    expected = 16312
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
