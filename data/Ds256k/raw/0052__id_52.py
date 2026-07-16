# Auto-extracted from ds_lt256k_500.jsonl
# record_id=52  entry=f  input='13'  output='833'  tokens=79881

def fn0(m, d):
    cnt = m + m
    aux = 17 + m
    cur = (d ^ cnt) & m
    t0 = (cnt - d) * cnt
    hi = t0 % 1009
    t1 = (hi ^ m) & 5 << 1
    cur = t1 ^ (m ^ 1) << 2
    hi = hi // 4
    t2 = (aux - 13) // 5 | aux
    return t2 % 65521

def f(x):
    nxt = [837, 549, 42, 71, 675, 768, 909, 856]
    t0 = nxt[x % 8] ^ x
    b = (x - 1 & t0) * x
    for val in range(9):
        for q in range(8):
            t1 = x | nxt[x % 8]
            t2 = nxt[b % 8] - q
            nxt[b % 8] = (t1 + t2) % 1009
            t3 = (x * 15 ^ x + 1) >> 3
            b = (t3 ^ q) & 32767
    nxt[b % 8] = x + b
    t4 = x + nxt[x % 8]
    aux = (b ^ 13 ^ t4) - x
    t5 = b * aux * (x * x)
    cur = t5 % 9973
    if b // 2 == 1:
        t6 = (x - cur) % 9973
        t7 = b // 6 % 4093
        aux = fn0(t6, t7)
        t8 = (aux - cur) % 9973
        t9 = cur ^ aux
        t10 = t9 & (x & b)
        aux = fn0(t8, t10)
    else:
        if aux - 13 <= 4:
            t11 = 10 * x * nxt[cur % 8]
            t12 = t11 // 7 % 9973
            t13 = (b - 4) % 4093
            b = fn0(t12, t13)
    t14 = nxt[b % 8]
    t15 = (t14 - 3) % 4093
    t16 = (b - cur) % 9973
    aux = fn0(t15, t16)
    for acc in range(11):
        aux = (aux >> 1 ^ aux) // 3 & 511
    lo = cur * b % 9973
    t17 = b + nxt[cur % 8]
    t18 = (b ^ 17) + (17 - aux)
    t19 = (t18 | b % 4093 & 13) & 65535
    aux = fn0(t17 % 9973, t19)
    for tot in range(61):
        t20 = (aux & 4) + aux
        t21 = t20 ^ x + 5
        lo = (t21 ^ tot) & 16383
    hi = 6 * x // 5
    u = x + nxt[lo % 8]
    tmp = x & 11
    t22 = tmp * aux ^ x + tmp
    return t22 % 9973

if __name__ == "__main__":
    arg = 13
    expected = 833
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
