# Auto-extracted from ds_lt256k_500.jsonl
# record_id=216  entry=f  input='6'  output='2'  tokens=108732

def f(x):
    tot = (x | 19) - x
    for y in range(5):
        v = 0
        while v < 10:
            t0 = (x & 19) + x
            t1 = (t0 << 2) + tot
            tot = t1 & 4095
            tot = ((15 ^ v) << 3) + x & 16383
            v = v + 1
    for m in range(12):
        nxt = 0
        while nxt < 18:
            x = (nxt | x) % 4093
            t2 = (20 | 13) * x
            t3 = t2 // 2 | nxt
            tot = t3 % 9973
            nxt = nxt + 1
    if 20 + x == 49:
        for g in range(6):
            tot = tot // 6 // 6 % 4093
            tot = (x + x - tot) % 4093
            t4 = g + x
            t5 = t4 | 16 ^ 15
            t6 = (tot & 16) * g
            x = (t5 + t6) % 4093
    t7 = x ^ tot | tot ^ 8
    return ((x ^ 19 | tot) ^ t7) & 32767

if __name__ == "__main__":
    arg = 6
    expected = 2
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
