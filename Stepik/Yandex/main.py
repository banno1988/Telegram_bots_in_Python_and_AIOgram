n = [4, 8, 15, 16, 3, 14, 15, 192, 168, 1992, 37, 256, 98, 101, 273, 7787, 918, 39, 1098, 222, 69, 96, 5234, 777]
print(n)
n1 = []
for i in n:
    if i % 2 == 0:
        n1.append(i ** 2)
    else:
        n1.append(i * 2)
print(n1)
n2 = []
for i in n1:
    if i % 24 != 0:
        n2.append(i)
print(n2)
n3 = [str(i) for i in n2]
print(n3)
min_number = sorted(n3)
max_number = sorted(n3, reverse=True)

min_number1 = ''.join(sorted(n3))
max_number1 = ''.join(sorted(n3, reverse=True))
# max_number11 = min_number[::-1]
print(max_number)
# print(max_number11)
print(min_number)

# print(max_number1)
# print(min_number1)
print(int(max_number1) + int(min_number1))

n4 = ['9604', '842724', '78', '74', '6', '65536', '64', '546', '49284', '30', '30', '27394756', '256', '202', '196',
      '16', '15574', '1554', '138', '1205604']
n5 = n4[::-1]
print(n4)
print(n5)
min_number2 = ''.join(n4)
max_number2 = ''.join(n5)
print(int(max_number2) + int(min_number2))

# n4 = ['8', '74', '6', '65536', '64', '60637369', '603729', '546', '49284', '30', '30', '256', '2196', '196', '196',
#       '1836', '1521', '138', '10468', '10201']
# n5 = ['10201', '10468', '138', '1521', '1836', '196', '196', '2196', '256', '30', '30', '49284', '546', '603729',
#       '60637369', '64', '65536', '6', '74', '8']
# min_number2 = ''.join(n5)
# max_number2 = ''.join(n4)
# print(max_number2)
# print(min_number2)
# print(int(max_number2) + int(min_number2))
# print(int(max_number1) + int(min_number1) - int(max_number2) - int(min_number2))


# n6 = ['9', '9604', '842724', '78', '74529', '512', '4761', '444', '32', '28', '27394756', '225', '225', '202', '16',
#       '16', '15574', '1554', '1369', '1205604']
# n7=n6[::-1]
# min_number3 = ''.join(n6)
# max_number3 = ''.join(n7)
# print(int(max_number3) + int(min_number3))
