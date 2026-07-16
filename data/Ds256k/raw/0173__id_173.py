# Auto-extracted from ds_lt256k_500.jsonl
# record_id=173  entry=f  input='12'  output='299'  tokens=103221

def rec(n, a):
    if n <= 0:
        return a
    for p in range(8):
        a = (a | 17) % 1009
        a = (p * n | a) & 1023
        for j in range(8):
            t0 = p ^ n | a
            a = t0 % 251
    t1 = a | n
    t2 = t1 | n + n
    return rec(n - 1, t2 % 1009)

def f(x):
    cnt = [4, 37, 110, 206, 27, 131, 9, 46]
    b = x + 1 - x
    w = (b ^ 7) - b - 10
    tot = 0
    while tot < 11:
        b = (b & w) + 6 & 511
        for cur in range(9):
            cnt[cur % 8] = b * 19 % 251
        tot = tot + 1
    t0 = cnt[x % 8] & b
    cnt[x % 8] = (t0 ^ x + w) % 251
    prv = 0
    while prv < 10:
        for p in range(17):
            cnt[p % 8] = cnt[w % 8] >> 3
            cnt[w % 8] = (b + x >> 1) + prv
            t1 = (prv & 7) + b
            t2 = b + 14 + prv
            cnt[x % 8] = t1 - t2
        x = (x ^ 12) & 511
        prv = prv + 1
    for z in range(6):
        x = (12 * w | z) & 262143
        x = (x - b) % 97
        t3 = (x | 15) % 251
        t4 = t3 ^ cnt[b % 8]
        cnt[b % 8] = t4 % 251
    t5 = w * b
    t6 = t5 + (w | b)
    cnt[x % 8] = (t6 | 18) % 251
    t7 = 11 + w
    g = t7 * (b + w)
    return (g + b) % 65521

if __name__ == "__main__":
    arg = 12
    expected = 299
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
