# Auto-extracted from ds_lt256k_500.jsonl
# record_id=245  entry=f  input='9'  output='361'  tokens=120417

def rec(n, a):
    if n <= 0:
        return a
    t0 = (17 & a) * n
    u = t0 & 32767
    t1 = (a + n) // 3
    b = (t1 | u) & 32767
    t2 = u // 5 >> 2
    t3 = t2 + (a - 18 >> 3) & 4095
    return rec(n - 1, t3)

def f(x):
    if x * x != 8:
        for prv in range(8):
            x = 16 * 16 + x & 1023
            t0 = 3 + 13 + x
            x = t0 & 131071
        x = (x & 17) + x
    t1 = x * x & 4095
    x = rec(58, t1)
    nxt = 0
    while nxt < 3:
        t2 = 3 * x + x
        t3 = nxt & 12 ^ nxt
        x = (t2 ^ t3) % 4093
        t4 = 19 | 6 | 2 | x
        x = t4 % 4093
        nxt = nxt + 1
    a = 0
    while a < 11:
        t5 = (16 & x) + a
        t6 = a & x ^ a
        x = (t5 ^ t6) & 511
        x = (x | 2) % 4093
        a = a + 1
    t7 = x // 5 - 3
    t8 = x + x - x
    cur = t7 ^ t8
    s = cur - 5 >> 3 & 1
    for idx in range(10):
        t9 = (s ^ 1) & x | idx
        cur = t9 & 65535
        for g in range(2):
            s = (12 - cur | s) & idx
    if 20 + s <= 19:
        t10 = (x - 16) // 8
        t11 = (t10 ^ x * x * cur) & 8191
        cur = rec(45, t11)
    e = 0
    while e < 154:
        t12 = s * x * (x ^ cur) - s
        cur = t12 & 4095
        e = e + 1
    return cur * cur & 8191

if __name__ == "__main__":
    arg = 9
    expected = 361
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
