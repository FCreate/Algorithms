def check(w, h, n, x):
    if ((x//w) * (x//h)) >= n:
        return True
    return False

w, h, n = list(map(int, input().split()))
l, r = -1, max(h,w) * n
while l+1 < r:
    mid = l + (r-l) // 2
    if check(w, h, n, mid):
        r = mid
    else:
        l = mid
print(r)