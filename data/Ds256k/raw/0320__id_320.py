# Auto-extracted from ds_lt256k_500.jsonl
# record_id=320  entry=f  input='7'  output='10'  tokens=213872

def fn0(e, c):
    s = [71, 73, 61, 88, 84, 4, 11]
    t = c + c
    t0 = s[t % 7]
    t1 = e | t0 | e
    res = t1 >> 4
    e = (11 ^ res) // 6 % 97
    for d in range(6):
        if 6 * res > 3:
            t2 = d + 10 & d
            t3 = t2 + (8 - 11) % 17 ^ e
            s[t % 7] = t3 % 97
            t4 = (res >> 3) - e // 6
            t = t4 - d & 2047
        else:
            t5 = s[res % 7]
            t6 = t - t5 - c
            c = t6 % 9973
        t7 = (4 | 3) + e
        res = (t7 ^ d) % 65521
    e = (e - c + c * t) % 97
    t8 = s[t % 7]
    t9 = e * t8 - t
    s[t % 7] = (t9 & 4095) % 97
    t10 = (t >> 2) + e
    return t10 % 9973

def f(x):
    for cur in range(4):
        nxt = 0
        while nxt < 7:
            x = ((13 | 11) - x) % 1009
            x = (11 - x) % 17
            t0 = nxt - x
            t1 = t0 - (6 - 16)
            x = t1 * x & 65535
            nxt = nxt + 1
    for a in range(7):
        for t in range(146):
            t2 = ((t | 8) << 3) + x
            x = t2 & 131071
        x = (x | 9) & 255
        x = ((a | x) ^ 8) % 17
    tmp = x ^ 8
    idx = tmp ^ 15
    t3 = (idx << 1) * 10 ^ tmp
    aux = t3 % 1009
    hi = idx * tmp & idx
    t4 = (idx & tmp) + hi
    t5 = t4 | (idx & 15) - aux
    t6 = idx >> 1
    t7 = t6 & hi << 3
    t8 = (t7 + idx) % 1009
    aux = fn0(t5 % 1009, t8)
    t9 = (aux & 14) + 5
    return t9 << 1 & 255

if __name__ == "__main__":
    arg = 7
    expected = 10
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
