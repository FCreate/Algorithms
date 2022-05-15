#https://codeforces.com/contest/1364/problem/A
t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    l, r, s = None, None, 0
    for i in range(len(arr)):
        if arr[i]%x:
            if l is None:
                l = i
            r = i
        s += arr[i]
    if l is None:
        print(-1)
    elif s%x:
        print(n)
    else:
        print(n-min(l+1, n-r))

