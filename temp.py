
# print(((lambda: int(input()))()) * ((lambda: int(input()))()))

#SN0WB@LL
# #CH1LL5
#C@NDYC@N3
#D3C0R@T1ON5
#REV3R5E
#S0RT3D
#SN0WFL@KE
# print(round((lambda v, t: ((((lambda c: (c * 9/5) + 32), (lambda f: (f - 32) * 5/9 ))[t == "C"])(v)))(int(input()), input()), 1))

# square = (lambda size: "\n".join(["*" * size for _ in range(1, size + 1)]))
# triangle = (lambda size: "\n".join(["*" * i for i in range(1, size + 1)]))

# def triangle(size):
#     return "\n".join(["*" * i for i in range(1, size + 1)])

# print(triangle(1))
# print(triangle(3))
# print(triangle(5))

# print(((lambda size: "\n".join(["*" * size for _ in range(1, size + 1)])), (lambda size: "\n".join(["*" * i for i in range(1, size + 1)])))[input() == "triangle"](int(input())))

# print("".join(i for i in reversed(input())))
# print("\n".join(i for i in sorted(input().split(","))))

# float(input()) / int()
print((lambda y, x: round(float(y) / int(x), 2) if int(x) != 0 else "You do not need to buy any presents!")(input(), input()))