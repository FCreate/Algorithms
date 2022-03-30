def check(m, workers, T):
    cnt = 0
    for worker in workers:
        baloon = worker[1] * (T//(worker[0]* worker[1] + worker[2])) + min((T%(worker[0]*worker[1]+worker[2]))/worker[0], worker[1])
        cnt += int(baloon)
    if cnt >= m:
        return True
    return False

m, n = list(map(int, input().split()))
workers = []
for _ in range(n):
    workers.append(list(map(int, input().split())))

l, r = -1, 1500000000000000000000
while l+1 < r:
    mid = l + (r-l) // 2
    if check(m, workers, mid):
        r = mid
    else:
        l = mid
print(l+1)
numberOfBaloons = []
for worker in workers:
    baloon = worker[1] * ((l+1) // (worker[0] * worker[1] + worker[2])) + min(
        ((l+1) % (worker[0] * worker[1] + worker[2])) / worker[0], worker[1])
    numberOfBaloons.append(int(baloon))
print(" ".join(list(map(str, numberOfBaloons))))