# Auto-extracted from ds_lt256k_500.jsonl
# record_id=56  entry=f  input='14'  output='59'  tokens=125508

def rec(n, a):
    if n <= 0:
        return a
    for q in range(9):
        a = (a ^ 1) + n + n & 65535
    t0 = 11 & n ^ n
    t1 = (t0 + a) % 251
    return rec(n - 1, t1)

def f(x):
    s = x * x + x + x
    nxt = 16 & x
    q = 7 & x
    for tot in range(240):
        t0 = 18 + x + s
        s = t0 % 1009
        t1 = s & 10 ^ nxt
        x = (t1 + x) % 97
        if q - s == 17:
            nxt = (6 + s - nxt) % 97
            t2 = 3 - nxt - tot
            q = t2 & 511
    t3 = (nxt >> 3) * (s | 19)
    t4 = t3 + ((nxt & s) - nxt)
    s = rec(58, t4 & 131071)
    if nxt - q > 19:
        for j in range(6):
            s = (q - s >> 3) % 251
            x = (x ^ j) % 17
        for buf in range(7):
            t5 = (buf - x) * s
            t6 = t5 * ((nxt - 13) // 6)
            s = t6 & 65535
            t7 = x - buf - (nxt ^ 15)
            s = t7 & 4095
            t8 = 14 - s + s
            q = (t8 | q) % 97
    else:
        nxt = (s ^ 3) + s
    t9 = 14 * x << 4
    return (t9 | q) % 251

if __name__ == "__main__":
    arg = 14
    expected = 59
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
