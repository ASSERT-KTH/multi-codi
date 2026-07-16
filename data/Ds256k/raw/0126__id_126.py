# Auto-extracted from ds_lt256k_500.jsonl
# record_id=126  entry=f  input='6'  output='883'  tokens=16653

def rec(n, a):
    if n <= 0:
        return a
    t0 = (12 ^ 5) - n + a
    j = t0 & 65535
    for z in range(3):
        t1 = (z ^ n) * n - a
        j = t1 % 9973
        t2 = (15 ^ 8) * (n >> 3) - j
        j = t2 % 251
        a = z + j & 32767
    t3 = j // 2 ^ a
    return rec(n - 1, t3 & 65535)

def fn0(e, g, m):
    t0 = e + g ^ g << 3
    t1 = (t0 - 15) % 251
    m = rec(71, t1)
    val = m // 7 >> 2
    for p in range(9):
        val = (val - 2) % 9973
        t2 = (p << 3 & 5 | 1) - e
        g = t2 & 2047
    t3 = m * 7 << 3
    t4 = (t3 ^ (g - e ^ g)) % 9973
    e = rec(56, t4)
    t5 = (20 - 1) * val
    return t5 + 17 & 2047

def f(x):
    s = [216, 156, 187, 195, 84, 46, 60, 122]
    b = x | 15
    t0 = s[x % 8]
    u = t0 | x
    s[u % 8] = b * x >> 2 & b
    b = 1 << 4 ^ u
    if 18 + b != 49:
        t1 = s[x % 8]
        b = t1 + u
        b = x * 6 * 12 << 1
    else:
        t2 = 14 - x + b
        b = t2 * (u - x)
    u = (b & u) // 8
    for q in range(51):
        if 9 - x > 25:
            t3 = b // 2
            t4 = t3 ^ 15 * 20
            t5 = (u - 20) * q
            t6 = t4 * t5 & 4095
            s[b % 8] = t6 % 251
            t7 = s[x % 8]
            t8 = 4 & b
            s[b % 8] = t8 & 15 - t7
        else:
            t9 = s[b % 8] * x
            x = (10 | q) & t9
            x = (b - 17 + x) % 9973
    return (6 & b ^ (x ^ u)) % 1009

if __name__ == "__main__":
    arg = 6
    expected = 883
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
