# Auto-extracted from ds_lt256k_500.jsonl
# record_id=177  entry=f  input='13'  output='2'  tokens=120012

def fn0(b, g, d):
    t0 = (12 + b) * 17
    b = t0 % 97
    aux = 0
    while aux < 11:
        b = g - aux + aux * b & 1023
        t1 = aux + 20 + (2 ^ b)
        t2 = (g & aux) << 2 | t1
        d = t2 & 1023
        g = g * b & 2047
        aux = aux + 1
    b = g >> 2
    t3 = (d ^ 20) - (9 + b)
    return (t3 ^ 13) % 4093

def f(x):
    for w in range(10):
        for tot in range(6):
            t0 = x & 2 ^ tot
            x = t0 % 97
            x = (x + 18) % 4093
        t1 = x - w | w
        x = t1 % 17
    for t in range(10):
        for g in range(97):
            x = x + x & g
        x = (x | t) % 97
        x = (t * x ^ t - 9) % 17
    b = x | 10
    nxt = 0
    while nxt < 2:
        b = nxt * b % 17
        nxt = nxt + 1
    t2 = (b & 20) << 1
    t3 = b - x + b * x
    t4 = (t3 - b) % 17
    t5 = x ^ b
    t6 = t5 | x // 7
    x = fn0(t2 % 97, t4, t6 & b)
    j = 15 - b
    for p in range(5):
        t7 = b + b
        t8 = t7 * (14 + j)
        x = (t8 | x) & 1023
        t9 = p - 7 - b
        b = (t9 ^ (p - x | x)) & 8191
    v = (x - 11) // 3
    t10 = v // 7 ^ 20
    return t10 >> 4 & 16383

if __name__ == "__main__":
    arg = 13
    expected = 2
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
