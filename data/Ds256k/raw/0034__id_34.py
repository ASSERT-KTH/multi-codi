# Auto-extracted from ds_lt256k_500.jsonl
# record_id=34  entry=f  input='9'  output='1'  tokens=35632

def f(x):
    if x - 7 == 26:
        x = x + 11 + x
        x = x * 5
    lo = (x ^ 9) + x
    for nxt in range(11):
        t0 = nxt - lo | x + 9
        x = (t0 - (nxt - lo << 2)) % 97
    if lo | 10 >= 37:
        if lo * lo != 51:
            lo = 7 ^ lo
            t1 = x + x + lo
            t2 = x * lo & x
            x = t1 + t2
        else:
            lo = x + x
        x = lo * lo & x
    for val in range(10):
        t3 = val << 1
        t4 = t3 - (val << 2)
        t5 = t4 // 4 + lo
        lo = t5 & 1023
        lo = (18 - lo | 9) % 4093
    for w in range(3):
        x = (w ^ lo) % 97
    for g in range(7):
        x = ((12 + x) // 2 - g) % 1009
        lo = lo // 5 % 1009
        t6 = lo + 8 >> 3 << 4
        lo = t6 % 1009
    v = 12 + x
    for q in range(5):
        t7 = (q | 9) ^ v
        v = t7 % 97
        prv = 0
        while prv < 12:
            lo = (prv ^ x) % 97
            v = (q * 5 + lo ^ v) & 2047
            prv = prv + 1
    cur = v // 4 - (x - 12)
    buf = (cur + v ^ v + cur) >> 3
    cnt = (x ^ 20) & cur
    a = cnt | 13
    return x + buf & 65535

if __name__ == "__main__":
    arg = 9
    expected = 1
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
