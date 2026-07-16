# Auto-extracted from ds_lt256k_500.jsonl
# record_id=138  entry=f  input='4'  output='207'  tokens=17919

def f(x):
    m = [58, 74, 41, 23]
    e = 20 & x ^ (x ^ 11)
    t = 0
    while t < 7:
        for z in range(9):
            t0 = e * 17 ^ x
            t1 = t0 * m[z % 4]
            m[x % 4] = t1 % 97
        t = t + 1
    for cur in range(8):
        x = cur * x % 251
    for b in range(3):
        x = x - b & 255
        t2 = (8 << 4) + e
        x = (t2 ^ x) & 4095
    nxt = (e ^ x) >> 3
    t3 = m[e % 4]
    t4 = (7 | e) ^ t3
    val = t4 >> 3
    t5 = e + nxt ^ 4 - e
    return (t5 - nxt) % 251

if __name__ == "__main__":
    arg = 4
    expected = 207
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
