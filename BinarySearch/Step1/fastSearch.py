def binarySearchRight(arr, x):
    l, r = -1, len(arr)-1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if arr[mid] >= x:
            r = mid
        else:
            l = mid
    return r + 1 if arr[r] >= x else len(arr)+1

def binarySearchLeft(arr, x):
    l, r = -1, len(arr)
    while l + 1 < r:
        mid = l + (r - l) // 2
        if arr[mid] <= x:
            l = mid
        else:
            r = mid
    return l+1 if arr[l] <= x else 0

input()
arr = list(map(int, input().split()));
arr.sort()
k = int(input())
queries = []
for _ in range(k):
    queries.append(list(map(int, input().split())))
answer = []
for q in queries:
    l = binarySearchRight(arr, q[0])
    r = binarySearchLeft(arr, q[1])
    answer.append(r-l+1)
print(" ".join(list(map(str, answer))))
