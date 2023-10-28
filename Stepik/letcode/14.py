def longestCommonPrefix(strs):
        a = min(strs, key=len)
        s=''
        for i in range(len(a)):
            for j in strs:
                if a[i]!=j[i]:
                    return s
                    break
            else:
                s=s+a[i]
        return s



print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["reflower","flow","flight"]))
print(longestCommonPrefix(["cir","car"]))
print(longestCommonPrefix(["aca","cba"]))