def condic(a, b, rez):
    if rez == 'fan':
        return a
    if rez == 'auto':
        return b
    if rez == 'heat':
        if b >= a:
            return b
        else:
            return a
    if rez == 'freeze':
        if b <= a:
            return b
        else:
            return a


a, b = [int(i) for i in input().split()]
rez = input()

print(condic(a, b, rez))
print(condic(-50, 50, 'heat'))
print(condic(-50, 50, 'freeze'))
print(condic(-50, 50, 'freeze'))
print(condic(-50, 50, 'freeze'))