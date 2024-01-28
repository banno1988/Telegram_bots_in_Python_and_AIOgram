def stringToStirng(a, b):
    if b not in a:
        return [-1]
    t=[]
    for i in range(len(a)):
        if a[i]==b[0] and len(a[i:])>=len(b):
            for j in range(1,len(b)):
                if a[i+j]!=b[j]:
                    break
            else:
                t.append(i)
    return t


print(*stringToStirng('abacabadaba','aba'))