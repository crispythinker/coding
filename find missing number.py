def fmn(arr):
    n = len(arr)
    expected = n * (n + 1) // 2
    actual = sum(arr)
    return expected - actual
print(fmn)