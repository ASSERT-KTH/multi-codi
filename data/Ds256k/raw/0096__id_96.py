# Auto-extracted from ds_lt256k_500.jsonl
# record_id=96  entry=f  input='5'  output='1552'  tokens=86086

def rec(n, a):
    if n <= 0:
        return a
    t0 = a * 4 | 19 | n
    idx = t0 % 65521
    prv = 0
    while prv < 4:
        t1 = a // 8 + n * n
        t2 = t1 * (prv - n - idx)
        a = t2 % 17
        prv = prv + 1
    for t in range(4):
        if idx + idx == 36:
            idx = (n + t) * idx & 32767
            a = t - a & 65535
        else:
            a = a & 19
    t3 = (7 ^ idx) - a & 65535
    return rec(n - 1, t3)

def f(x):
    q = 0
    while q < 30:
        for res in range(6):
            t0 = (res - 14) * (q - res)
            t1 = t0 - (q + 8) * q
            x = (t1 ^ x) % 65521
            t2 = (20 << 2 ^ q) - x
            x = t2 & 131071
        t3 = x ^ q ^ x
        x = t3 & 16383
        x = (q * q ^ x) & 255
        q = q + 1
    b = x - 4
    t4 = (11 ^ x) * b
    z = t4 + b & 16383
    prv = x - z - (z ^ b)
    for y in range(2):
        for d in range(8):
            x = (z * b ^ x) % 4093
        x = ((x | 7) + 8) * z % 4093
    cur = 0
    while cur < 12:
        t5 = b & cur & (cur ^ 20)
        t6 = (20 - z) * (cur << 3)
        x = t5 - t6 & 16383
        z = (b - 2) * (z - prv) & 1023
        cur = cur + 1
    x = prv * 7 % 65521
    t7 = (prv | z) ^ 12
    return t7 & 2047

if __name__ == "__main__":
    arg = 5
    expected = 1552
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
