def binarySearch(arr, x):
    l, r = -1, len(arr)
    while l+1<r:
        mid = l + (r-l) // 2
        if arr[mid] == x:
            return True
        if arr[mid] >= x:
            r = mid
        else:
            l = mid
    return False
input()
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for q in queries:
    if binarySearch(arr, q):
        print("YES")
    else:
        print("NO")