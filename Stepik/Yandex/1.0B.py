def treugol(a, b, c):
    if a == b == c:
        return "YES"
    if a + b > c and a + c > b and b + c > a:
        return 'YES'
    else:
        return "NO"


a, b, c = [int(input()) for i in range(3)]

print(treugol(a, b, c))

print(treugol(1, 1, 1))
print(treugol(0, 1, 1))
print(treugol(10, 20, 30))
