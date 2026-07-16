# Auto-extracted from ds_lt256k_500.jsonl
# record_id=234  entry=f  input='9'  output='13'  tokens=218270

def rec(n, a):
    if n <= 0:
        return a
    for y in range(5):
        t0 = a << 3
        t1 = t0 * (2 - n)
        t2 = y - n | t1
        a = t2 % 4093
    if a >> 2 < 64:
        for lo in range(9):
            a = (a >> 3) // 4 * lo & 1023
            t3 = lo & n ^ lo ^ a
            a = t3 % 9973
            a = (a ^ n) % 4093
    a = (n ^ 18) - a & 131071
    t4 = n * a % 4093
    return rec(n - 1, t4)

def f(x):
    q = [141, 193, 104, 9]
    for m in range(197):
        q[x % 4] = x - m
        t0 = (m * x + x) // 7
        x = t0 % 97
    t1 = x * 7
    t2 = t1 & x - 12
    aux = t2 - x
    x = (10 & aux) - x >> 2
    t3 = ((x ^ aux) << 4) % 97
    x = rec(118, t3)
    x = (aux & 8) * x
    t4 = q[x % 4] * x - aux
    x = t4 % 251
    b = 0
    while b < 2:
        q[b % 4] = (x + aux) % 251
        b = b + 1
    x = 19 ^ aux | aux - 3
    t5 = 4 ^ q[x % 4]
    t6 = t5 | q[x % 4] // 7
    return (t6 ^ aux) % 97

if __name__ == "__main__":
    arg = 9
    expected = 13
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
