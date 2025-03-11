def egyptian_mul(a, b):
    res = 0
    while True:
        if a % 2 == 1:
            res += b
        a = a // 2
        b = b * 2
        if a == 1:
            res += b
            break
    return res
print(egyptian_mul(int(input()), int(input())))