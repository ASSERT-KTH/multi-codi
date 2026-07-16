# Auto-extracted from ds_lt256k_500.jsonl
# record_id=55  entry=f  input='17'  output='242'  tokens=40778

def f(x):
    for a in range(12):
        t0 = (a * x & x) << 3
        x = t0 % 4093
        w = 0
        while w < 11:
            t1 = x * x
            t2 = t1 * (a ^ 8)
            x = t2 // 4 % 9973
            w = w + 1
    aux = (x % 4093 ^ x) - x
    lo = aux // 8 << 3
    for acc in range(9):
        t3 = x + x & acc * 11
        t4 = x + lo | aux | t3
        aux = t4 % 251
        if acc << 1 ^ lo <= 41:
            t5 = (17 + acc) * x - x
            lo = t5 % 251
            lo = (acc | x) & 131071
        else:
            t6 = lo >> 1
            t7 = t6 * (lo ^ aux)
            aux = (t7 | 14) & 2047
        lo = ((13 | aux) ^ acc) & 1023
    j = 19 - 6 | aux
    q = (aux & x ^ 6) // 4
    nxt = j // 8 - j >> 2
    t8 = lo - 12 - 4
    return (t8 | (12 - x) * j) % 251

if __name__ == "__main__":
    arg = 17
    expected = 242
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
