def check(arr, k, x):
    numberRopes = 0
    for elem in arr:
        numberRopes += elem // x
    if numberRopes >= k:
        return True
    return False

n, k = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(int(input()))

l, r = 0, max(arr) + 1
while abs(r-l) > 10**(-8):
    mid = l + (r-l) / 2
    if check(arr, k,  mid):
        l = mid
    else:
        r = mid
print(r)