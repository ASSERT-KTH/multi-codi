# Auto-extracted from ds_lt256k_500.jsonl
# record_id=446  entry=f  input='14'  output='223'  tokens=200361

def f(x):
    for buf in range(10):
        nxt = 0
        while nxt < 2:
            t0 = (buf | 18) - x
            t1 = t0 | nxt * buf * 9
            x = t1 % 9973
            x = (nxt & 4 | x) % 65521
            nxt = nxt + 1
    p = x | 6
    for z in range(74):
        p = (p - 11 | x) % 65521
        c = 0
        while c < 7:
            x = (x ^ 10) % 251
            t2 = z ^ p ^ x + c
            p = t2 & 32767
            c = c + 1
    for s in range(11):
        t3 = p * p | x
        x = t3 % 251
        t4 = s * x // 4
        p = (t4 - p) % 65521
        x = x * x & 511
    if x * p <= 50:
        for w in range(11):
            x = (w + p) % 9973
            x = (x ^ 15) % 9973
        for lo in range(9):
            x = p & lo
    else:
        t5 = p * p + (1 - p)
        p = t5 % 251
        p = (2 + x + p) % 65521
    return ((13 | 20) & 9 | p) % 251

if __name__ == "__main__":
    arg = 14
    expected = 223
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
