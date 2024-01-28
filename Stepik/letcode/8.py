def myAtoi(s: str) -> int:
    t = ''
    for i in s.lstrip():
        if i.isalpha() or i == '.' or i == ' ':
            break
        if i == '-' and len(t) > 0:
            break
        if i == '+' and len(t) > 0:
            break

        if i.isdigit() or i == '-' or i == '+':
            t += i
    if t == '' or t == '+' or t == '-':
        t = 0
    elif int(t) > (2 ** 31 - 1):
        t = 2 ** 31 - 1
    elif int(t) < -(2 ** 31):
        t = -(2 ** 31)
    return int(t)


print(myAtoi('3.14159'))
