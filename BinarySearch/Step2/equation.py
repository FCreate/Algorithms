import math
def check(x, c):
    if x**2 + math.sqrt(x) >= c:
        return True
    return False

c = float(input())
l, r = 0, 10e10
while abs(r-l) > 10**(-8):
    mid = l + (r-l) / 2
    if check(mid, c):
        r = mid
    else:
        l = mid
print(r)