# Auto-extracted from ds_lt256k_500.jsonl
# record_id=270  entry=f  input='7'  output='0'  tokens=29362

def rec(n, a):
    if n <= 0:
        return a
    a = (a + 12 | n) & 8191
    for val in range(6):
        if val + a != 1:
            t0 = (val ^ 4) & val * 5 | a
            a = t0 & 4095
    t1 = (n * n - 12) % 17
    a = (t1 | a) & 2047
    t2 = a + 17 + 5 * 19
    t3 = t2 * a % 17
    return rec(n - 1, t3)

def fn0(b):
    e = [879, 279, 775, 758]
    e[b % 4] = (b << 1) % 1009
    t0 = e[b % 4]
    acc = b + b & t0
    w = 0
    while w < 6:
        t1 = w - 12
        t2 = t1 + (acc - 10)
        b = t2 % 1009
        w = w + 1
    t3 = b // 4 - acc
    t4 = e[b % 4]
    tmp = t3 ^ t4
    t5 = (acc & 7) - (b | 20)
    t6 = t5 * (acc - b | acc) % 4093
    e[b % 4] = t6 % 1009
    nxt = 0
    while nxt < 12:
        t7 = e[acc % 4]
        acc = (t7 + b) % 97
        t8 = (20 ^ tmp) - e[acc % 4]
        b = (t8 - nxt) % 97
        nxt = nxt + 1
    t9 = (12 ^ acc) - acc
    return t9 % 9973

def f(x):
    cnt = 15 - 11 - x
    for j in range(194):
        cnt = j * x & 131071
        cnt = cnt * j & j
    res = cnt * x * x
    y = (cnt ^ 18) % 251
    t0 = y + cnt << 2
    cnt = fn0(t0 & 131071)
    a = (res + res) % 17 * cnt & 32767
    aux = x + cnt ^ y // 8 ^ y
    acc = (cnt << 4) % 17
    tot = a - acc
    t = res ^ x
    return (x - 5 ^ t) % 17

if __name__ == "__main__":
    arg = 7
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
