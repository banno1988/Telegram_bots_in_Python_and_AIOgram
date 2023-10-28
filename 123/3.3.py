def binary_search(array, x):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


n = int(input())
stickers = sorted(set(map(int, input().split())))
k = int(input())
p = map(int, input().split())
for pi in p:
    pos = binary_search(stickers, pi)
    print(pos)
