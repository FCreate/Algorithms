def binarySearchLeft(arr, x):
    l, r = -1, len(arr)
    while l + 1 < r:
        mid = l + (r - l) // 2
        if arr[mid] <= x:
            l = mid
        else:
            r = mid
    return l + 1 if arr[l] <= x else 0


input()
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for q in queries:
    print(binarySearchLeft(arr, q))
