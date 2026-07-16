# Auto-extracted from ds_lt256k_500.jsonl
# record_id=385  entry=f  input='13'  output='832'  tokens=60530

def fn0(g):
    tmp = (g ^ 7) * g & 4095
    tmp = (5 | g) + 15
    g = 12 - 7 - g
    for val in range(7):
        tmp = (val | g) + tmp & 262143
    t0 = (g ^ 12) + (3 + g)
    tmp = t0 ^ tmp - g >> 3
    t1 = g ^ 6
    t2 = t1 + (g & tmp)
    tmp = t2 - 1
    t3 = g * tmp * g - tmp
    g = t3 % 17
    return (g - tmp) % 1009

def f(x):
    if x + x < 33:
        if 5 | x != 27:
            x = x & 11 ^ x & 18
            x = fn0(x * x & 262143)
        else:
            x = fn0(x // 4 % 97)
            x = fn0(x + 16 & 131071)
    b = 0
    while b < 51:
        x = (1 - x) % 9973
        tmp = 0
        while tmp < 7:
            x = b + x & 1023
            x = (b * b << 2 ^ x) % 97
            x = x & b
            tmp = tmp + 1
        b = b + 1
    t0 = x * x // 7
    nxt = t0 & 2047
    v = nxt + x
    nxt = (x * v + v) % 9973
    nxt = x & nxt
    return x * v % 1009

if __name__ == "__main__":
    arg = 13
    expected = 832
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
