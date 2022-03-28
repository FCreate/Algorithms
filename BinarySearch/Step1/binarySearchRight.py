def binarySearchRight(arr, x):
    l, r = -1, len(arr)-1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if arr[mid] >= x:
            r = mid
        else:
            l = mid
    return r + 1 if arr[r] >= x else len(arr)+1


input()
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for q in queries:
    print(binarySearchRight(arr, q))
