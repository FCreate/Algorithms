def check(n, x, y, mid):
    mid -= min(x, y)
    numberOfPapers = mid // x + mid//y
    if numberOfPapers + 1 >= n:
        return True
    return False

m, n = list(map(int, input().split()))
workers = []
for _ in range(n):
    workers.append(list(map(int, input().split())))

l, r = 0, n*max(x,y)
while l+1 < r:
    mid = l + (r-l) // 2
    if check(n, x, y, mid):
        r = mid
    else:
        l = mid
print(l+1)