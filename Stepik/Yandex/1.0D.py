a, b, c = [int(input()) for i in range(3)]


def rech(a, b, c):
    if c < 0:
        return 'NO SOLUTION'
    if a == 0 and b == 0 and c == 0:
        return 'MANY SOLUTIONS'
    if a != 0:
        return int((c ** 2 - b) / a)
    if a == 0 and b!= c**2:
        return 'NO SOLUTION'
    else:
        return 'MANY SOLUTIONS'

print(rech(a, b, c))
