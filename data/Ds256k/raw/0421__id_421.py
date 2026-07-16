# Auto-extracted from ds_lt256k_500.jsonl
# record_id=421  entry=f  input='3'  output='218'  tokens=31176

def f(x):
    t = [828, 860, 460, 867, 54, 452, 119, 19]
    tmp = x * x // 2
    buf = tmp * t[tmp % 8]
    for tot in range(385):
        if x + tmp >= 33:
            t[tmp % 8] = x * buf & 511
            t0 = t[tot % 8] - tot
            x = (t0 + tmp - x) % 65521
    g = buf + x + x - x
    t[buf % 8] = tmp & 11
    x = (x & 10) - 18
    x = (buf >> 2) * tmp % 65521
    buf = (x & 12 | g) % 4093
    t1 = 3 - 4 + buf
    return t1 & 2047

if __name__ == "__main__":
    arg = 3
    expected = 218
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
