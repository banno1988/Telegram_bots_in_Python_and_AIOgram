k = int(input())
t=k
s = input()
n = len(s)
max_beauty = 1

for l in range(n):
    r = l + 1
    while r < n:
        #print(r,k)
        if s[r] == s[l]:

            r += 1
        else:
            k -= 1
            r += 1
        if k<0:
            break
    if k==0:
        r+=1
    k=t
    #print(r)
    cur_beauty = r - l -1

    #print('#',max_beauty, cur_beauty)
    max_beauty = max(max_beauty, cur_beauty)

print(max_beauty)

# # пытаемся увеличить красоту строки, заменяя символы в текущей подстроке
# while k > 0 and l > 0 and r < n and cur_beauty < max_beauty + 1:
#     k -= 1
#     l -= 1
#     r += 1
#     cur_beauty += 2
#
# if k == 0 or cur_beauty >= max_beauty + 1:
#     break
# # вычисляем длину текущей подстроки и обновляем максимальную красоту строки
# cur_beauty = r - l
# max_beauty = max(max_beauty, cur_beauty)