# Auto-extracted from ds_lt256k_500.jsonl
# record_id=232  entry=f  input='19'  output='241'  tokens=10540

def rec(n, a):
    if n <= 0:
        return a
    t0 = (a & n) - n
    hi = t0 >> 1 & 65535
    val = (a - n ^ 10) & 131071
    t1 = (hi ^ a) - a & 4095
    return rec(n - 1, t1)

def f(x):
    buf = [54, 100, 173, 17]
    if x & 4 == 2:
        for p in range(2):
            t0 = x + buf[p % 4] + 8
            x = t0 & 8191
            t1 = (18 | 8) - p ^ x
            x = t1 & 1023
            t2 = x % 251 | p ^ x
            x = t2 % 251
    t = x // 3 | x
    z = (t * 19 ^ x + x) + x
    t3 = buf[x % 4] // 8
    buf[x % 4] = x // 4 * t3 % 251
    t4 = (buf[z % 4] - 1) * t
    buf[z % 4] = t4 % 65521 % 251
    c = z ^ 11
    for d in range(26):
        t5 = (z ^ 2) + z * 12
        t = (t5 + x + t) % 65521
        t6 = c - buf[x % 4]
        t = (t6 | d) & 255
    t7 = (z >> 4) - buf[t % 4]
    return (t7 >> 3) % 251

if __name__ == "__main__":
    arg = 19
    expected = 241
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
