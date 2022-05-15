#https://codeforces.com/contest/1520/problem/D?locale=ru
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}
    res = 0
    for i in range(n):
        elem = arr[i] - i
        if elem in d:
            res += d[elem]
        d[elem] = d.get(elem, 0) + 1
    print(res)


