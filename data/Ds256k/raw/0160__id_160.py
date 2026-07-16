# Auto-extracted from ds_lt256k_500.jsonl
# record_id=160  entry=f  input='11'  output='0'  tokens=50490

def f(x):
    val = (x - 14 | x) * x
    prv = x * 9
    t0 = prv - x
    t1 = t0 - prv * x
    t2 = (val ^ 20) + x
    cur = t1 + t2
    for z in range(7):
        for m in range(51):
            x = (z * z ^ prv ^ m) & 131071
    t3 = (x ^ prv) & (x & 17)
    return cur * 4 + x & t3

if __name__ == "__main__":
    arg = 11
    expected = 0
    got = f(arg)
    assert got == expected, f"f({arg!r}) = {got!r}, expected {expected!r}"
    print(f"f({arg!r}) = {got!r} OK")
