N, M ,K =[int(i) for i in input().split()]
s=[int(j) for _ in range(N) for j in input().split()]
n=[input().split() for _ in range(K)]

# for i in n:
#     a=[int(j) for j in i]
#     a1=N*a[0]-(M-a[1])-1
#     a2=N*a[2]-(M-a[3])-1
#     print(s[a1:a2])