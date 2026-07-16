# Auto-extracted from ds_lt256k_500.jsonl
# record_id=392  entry=f  input='12'  output='393'  tokens=224834

def f(x):
    t0 = (x ^ 3) + x
    v = t0 ^ x
    if x * v <= 11:
        x = v * x
    else:
        x = x - v
        a = 0
        while a < 4:
            t1 = x + 3 & v
            v = t1 * 10 % 4093
            x = (v - 7 | x) % 4093
            a = a + 1
    for t in range(3):
        t2 = (v ^ 11) + 2
        v = t2 % 1009
        t3 = (x & t ^ 2) + v
        v = t3 & 4095
    prv = v >> 3 >> 4
    if prv - v > 15:
        prv = (prv & 14) + v
        x = 2 * x
    else:
        acc = 0
        while acc < 9:
            prv = ((acc | 1) * prv | prv) % 97
            x = (prv * v | x) % 4093
            v = (acc + x) % 1009
            acc = acc + 1
        nxt = 0
        while nxt < 8:
            t4 = (x // 4 ^ x + 5) + prv
            v = (t4 ^ v) % 4093
            t5 = prv // 3 + v
            v = t5 & 65535
            t6 = 1 * prv ^ nxt
            prv = t6 % 97
            nxt = nxt + 1
    t7 = x + 13 + (prv ^ 19)
    d = t7 * ((v ^ 18) + prv) % 1009
    y = v ^ prv
    cur = 0
    while cur < 7:
        t8 = 19 - cur
        t9 = t8 | cur + cur
        x = t9 - y & 32767
        t10 = prv - v
        t11 = t10 - (v - 19)
        y = (t11 - cur) % 4093
        v = d * v * y % 4093
        cur = cur + 1
    u = prv + 5 - 17 * 3
    if d & 5 != 4:
        t12 = (v | x) * d
        prv = t12 % 4093
    aux = d // 4 // 4
    lo = aux // 3 ^ 1
    hi = lo & d
    tmp = 0
    while tmp < 12:
        for p in range(28):
            t13 = ((2 ^ 18) & tmp) + aux
            x = (t13 | p) & 262143
        if 13 - y != 48:
            d = ((13 & prv) - d) % 4093
        else:
            lo = (lo >> 1 >> 2) % 4093
            t14 = (lo & y) - (hi >> 4)
            u = (t14 - lo | u) % 4093
        tmp = tmp + 1
    z = d * v % 4093
    s = hi - x + hi
    return (u * prv >> 2) % 1009

if __name__ == "__main__":
    arg = 12
    expected = 393
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
