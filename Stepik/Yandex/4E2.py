n = int(input())
r = int(input())
t = [int(input()) for i in range(r)]

chel = 0
taimer = 0
k = 1
for i in range(r):
    if t[r - i - 1] == 0 and k:
        continue
    else:
        k = 0
    if taimer == 0:
        taimer += r - i
    else:
        taimer += 1
    while t[r - i - 1] > 0:
        if t[r - i - 1] > n - chel:
            t[r - i - 1] -= n - chel
            taimer += (r - i) * 2
            if t[r - i - 1] > 2 * n:
                taimer += (t[r - i - 1] - n) // n * (r - i) * 2
                t[r - i - 1] = (t[r - i - 1] % n) + n
            chel = 0
        else:
            chel += t[r - i - 1]
            t[r - i - 1] = 0
            if chel == n:
                k = 1
                rt = 0
                while (r - i - 1 - rt) > 0 and t[r - i - 1 - rt] == 0:
                    rt += 1
                taimer += (r - i) + r - i - rt - 1
                chel = 0
            else:
                if i == r-1:
                    taimer += 1
                else:
                    for j in range(r-i-1,-1,-1):
                        if t[j]!=0:
                            break
                    else:
                        k=1
                        taimer += (r - i)
print(taimer)
