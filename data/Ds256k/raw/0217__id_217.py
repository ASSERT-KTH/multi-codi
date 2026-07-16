# Auto-extracted from ds_lt256k_500.jsonl
# record_id=217  entry=f  input='6'  output='0'  tokens=89108

def rec(n, a):
    if n <= 0:
        return a
    t0 = n // 3 >> 3
    t1 = (a + a) // 5
    a = t0 & t1
    t2 = n - 10 ^ n - 8
    t3 = (t2 + a) % 4093
    return rec(n - 1, t3)

def f(x):
    prv = [652, 965, 312, 836, 47, 387, 509]
    c = x - 5
    d = 2 * prv[x % 7]
    prv[d % 7] = (prv[d % 7] | 11) % 1009
    if d | c > 40:
        aux = 0
        while aux < 7:
            t0 = prv[c % 7] + c - x
            d = (t0 ^ aux) & 1023
            aux = aux + 1
        if d & prv[x % 7] != 49:
            t1 = prv[d % 7]
            prv[c % 7] = (t1 | 10) % 1009
        else:
            prv[d % 7] = c - 1
    else:
        c = d + x
    t2 = d // 8
    t3 = 1 - x << 1
    t4 = t2 + (c & 5)
    tot = t3 * t4
    t5 = c * 20 - (d - 17)
    a = t5 ^ (x << 1) * c
    t6 = (x + tot) * 9
    q = t6 // 8
    for cur in range(141):
        t7 = (prv[d % 7] >> 3) + cur
        tot = t7 % 9973
        t8 = prv[q % 7] | a
        a = t8 * (x << 2) % 9973
    t9 = tot - 7
    t10 = t9 ^ (tot ^ 5)
    acc = t10 & 10
    t11 = q * a
    t12 = t11 + (c >> 2)
    b = t12 % 9973
    if a ^ 7 == 1:
        a = d ^ 7
        if prv[d % 7] >> 2 != 33:
            tot = acc & a
            t13 = q ^ tot
            t14 = t13 ^ tot // 4
            q = rec(54, t14 % 1009)
    t15 = c >> 4 >> 3
    return t15 & 262143

if __name__ == "__main__":
    arg = 6
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
