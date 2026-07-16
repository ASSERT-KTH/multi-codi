# Auto-extracted from ds_lt256k_500.jsonl
# record_id=336  entry=f  input='3'  output='19'  tokens=54188

def fn0(d):
    cur = 4 - 12 << 2 ^ d
    tmp = 0
    while tmp < 2:
        cur = ((cur << 4) * tmp ^ 8) & 32767
        tmp = tmp + 1
    if d * d > 52:
        val = 0
        while val < 2:
            t0 = d ^ 10
            t1 = t0 ^ d & 15
            d = t1 & 16383
            cur = ((d & val) - d) % 17
            val = val + 1
        t2 = (cur - d & d - 7) << 4
        d = t2 % 9973
    else:
        t3 = (d - cur) * d
        d = t3 * (cur // 8 ^ d) % 97
    nxt = (cur ^ 5) + d % 17
    g = (nxt & 18) - 12
    u = 0
    while u < 10:
        t4 = ((cur | g) & (1 | cur)) * nxt
        cur = t4 % 97
        if 10 - cur != 15:
            d = (18 | 3 | cur | d) % 97
        t5 = nxt - cur - 12
        cur = t5 % 17
        u = u + 1
    nxt = 6 + 4 ^ d
    t6 = (cur >> 1) * 14
    return t6 & 16383

def f(x):
    acc = 0
    while acc < 11:
        tot = 0
        while tot < 6:
            x = (x ^ tot | 19) & tot + x
            x = x * 5 & 4095
            x = x * acc % 97
            tot = tot + 1
        val = 0
        while val < 20:
            x = (val + val - x) % 65521
            val = val + 1
        x = (acc ^ x) % 97
        acc = acc + 1
    x = fn0(x + x & 131071)
    g = x - 17
    t0 = g - 14
    t1 = t0 - (18 << 1)
    x = fn0(t1 // 5 & 511)
    j = g >> 2 ^ x
    t2 = (j >> 2) * g
    lo = t2 & x
    aux = 1 & j ^ g
    return (j + j) % 97

if __name__ == "__main__":
    arg = 3
    expected = 19
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
