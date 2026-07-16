# Auto-extracted from ds_lt256k_500.jsonl
# record_id=324  entry=f  input='8'  output='17396'  tokens=76162

def f(x):
    prv = [80, 689, 155, 695, 662]
    y = x * x * prv[x % 5]
    if 5 - y >= 8:
        x = y + y
        for c in range(2):
            t0 = c * 8 + (x ^ c)
            y = t0 * ((x & 10) + c) % 65521
    else:
        t1 = prv[x % 5] >> 1
        y = (x // 5 | t1) % 1009
    j = (x & 8) * (10 << 2) & y
    val = y | 10
    for lo in range(18):
        t2 = val * prv[y % 5]
        prv[val % 5] = (t2 << 4) // 4 % 1009
        for nxt in range(9):
            y = (y + x ^ lo) & 4095
            t3 = val // 7 * (x // 2)
            j = t3 + 17 - nxt & 8191
            prv[val % 5] = (nxt + j - lo) % 1009
        t4 = val + val >> 1 | lo
        x = t4 % 65521
    prv[val % 5] = (x >> 1 ^ j) % 1009
    prv[val % 5] = (j + val) % 1009
    if j - prv[y % 5] != 57:
        j = 20 - val
    else:
        for buf in range(7):
            j = (val - y + j) % 65521
            t5 = prv[x % 5] * buf
            t6 = (val + y + t5 ^ buf) & 32767
            prv[j % 5] = t6 % 1009
            prv[y % 5] = y % 1009
    t7 = j - y
    t8 = t7 * (7 - x)
    return t8 % 65521

if __name__ == "__main__":
    arg = 8
    expected = 17396
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
