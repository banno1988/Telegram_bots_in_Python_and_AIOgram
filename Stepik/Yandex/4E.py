n = int(input())
r = int(input())
t = [int(input()) for i in range(r)]

chel = 0
taimer = 0
for i in range(r):
    if sum(t) == 0:
        break
    taimer += 1
    while t[i] > 0:
        if t[i] >= n - chel:
            t[i] -= n - chel
            if sum(t) > 0:
                taimer += (i + 1) * 2
            else:
                taimer += (i + 1)
            chel = 0
        else:
            chel += t[i]
            t[i] = 0
            if chel == n:
                if sum(t) > 0:
                    taimer += (i + 1) * 2
                else:
                    taimer += (i + 1)
                chel = 0
            else:
                if sum(t) == 0:
                    taimer += (i + 1)
                # else:
                #     taimer += 1

print(taimer)
