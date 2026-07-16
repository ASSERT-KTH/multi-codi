# Auto-extracted from ds_lt256k_500.jsonl
# record_id=31  entry=f  input='10'  output='801'  tokens=27065

def rec(n, a):
    if n <= 0:
        return a
    a = (4 + a) % 17
    t0 = a - 19 & 2047
    return rec(n - 1, t0)

def fn0(j):
    acc = 9 & 3 | j
    for z in range(8):
        idx = 0
        while idx < 5:
            t0 = z ^ 13 | j
            acc = t0 - idx & 2047
            acc = (acc - 1 >> 2) % 251
            t1 = j + z | (j | idx)
            j = t1 % 17
            idx = idx + 1
    acc = (acc ^ 15) >> 4 ^ acc
    t2 = 4 + acc - acc % 17
    j = rec(36, t2 & 2047)
    return (acc // 5 ^ j) & 255

def f(x):
    tot = [88, 218, 122, 206, 181, 106]
    t0 = tot[x % 6] ^ 7
    buf = t0 * 4
    for cnt in range(18):
        buf = buf & 4
        for acc in range(5):
            t1 = buf % 97 * x
            tot[buf % 6] = t1 * acc % 251
        t2 = tot[cnt % 6] ^ 19
        t3 = x * x * (cnt - 1)
        buf = ((t2 | 19) ^ t3) % 9973
    x = 6 ^ x
    if tot[buf % 6] >> 2 == 19:
        buf = 18 * x + buf // 3
        buf = buf * x * x % 1009
    t4 = 8 & buf
    x = t4 & buf * 15
    t5 = buf // 5 * 12
    return t5 % 1009

if __name__ == "__main__":
    arg = 10
    expected = 801
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
