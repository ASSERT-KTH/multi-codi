# Auto-extracted from ds_lt256k_500.jsonl
# record_id=332  entry=f  input='10'  output='41936'  tokens=123136

def f(x):
    m = 4 + x
    aux = x + x << 2
    t0 = 11 << 3
    t1 = t0 | m * m
    v = t1 & m
    q = x
    a = aux >> 1
    if x - 13 > 16:
        a = 11 + 5 & m
        g = 0
        while g < 10:
            q = (v * q + m ^ q) & 255
            t2 = (13 & x ^ v) - g
            aux = t2 % 97
            t3 = 9 + x ^ g
            v = t3 & 32767
            g = g + 1
    e = (aux | q) - q
    t4 = (11 ^ 4) - x * v
    t5 = (a - aux) * (m | aux)
    acc = t4 + t5
    t6 = x << 2 ^ 6 << 2
    j = t6 & (q >> 2) - 12
    b = 2 & 14 ^ aux
    buf = b * x
    tot = 0
    while tot < 9:
        for cnt in range(21):
            t7 = ((q | tot) - q * 4) * x
            b = (t7 + cnt) % 65521
            t8 = 12 + x ^ acc
            acc = t8 % 97
        tot = tot + 1
    val = e // 3
    d = q * 19
    t9 = x - e | acc ^ j
    prv = t9 + (d * aux + 13)
    return b * aux & 65535

if __name__ == "__main__":
    arg = 10
    expected = 41936
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
