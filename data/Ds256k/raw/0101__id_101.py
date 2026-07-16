# Auto-extracted from ds_lt256k_500.jsonl
# record_id=101  entry=f  input='20'  output='61841'  tokens=19087

def fn0(b, j):
    cur = j * j % 17
    tmp = 0
    while tmp < 4:
        t0 = j ^ b
        t1 = t0 + (b + b)
        cur = (t1 ^ tmp) % 4093
        for buf in range(9):
            b = (1 | j | buf) % 4093
            cur = tmp - cur & 255
        tmp = tmp + 1
    hi = b % 4093
    if j + 1 == 29:
        for q in range(3):
            t2 = (cur | 2) % 4093 + q
            j = t2 & 4095
    else:
        t3 = b - cur
        t4 = t3 ^ cur - j
        cur = t4 & cur
    e = (hi + j - cur) // 2
    t5 = hi - 8 >> 3
    return t5 & 131071

def f(x):
    cur = x - 17
    if x & cur <= 7:
        for j in range(11):
            cur = cur * x & x
            t0 = cur | j
            t1 = t0 + (cur + x)
            cur = t1 + cur & 262143
    d = 0
    while d < 29:
        t2 = (d & x) + d
        x = t2 % 17
        cur = ((15 ^ 4) - cur) % 65521
        d = d + 1
    t3 = (cur >> 3) - x
    t4 = cur - x ^ x + x
    t5 = (x + x << 1 ^ t4) % 251
    x = fn0(t3 & 16383, t5)
    t6 = cur * x ^ 10
    c = t6 % 251
    t7 = (cur // 2 - (1 ^ c)) * x
    a = t7 % 65521
    return ((c ^ a) - (cur - c)) % 65521

if __name__ == "__main__":
    arg = 20
    expected = 61841
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
