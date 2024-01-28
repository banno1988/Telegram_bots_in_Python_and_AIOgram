def reverse(x: int) -> int:
    t = 0
    k = 1
    if x < 0:
        x = abs(x)
        k = -1
    while x != 0:
        t = x % 10 + t * 10
        x = x // 10
    if t>2**31:
        return 0
    return t * k


print(reverse(1534236469))
