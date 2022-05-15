#https://codeforces.com/problemset/problem/1285/B?locale=ru
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = 0
    answer = "YES"
    for i in range(n-1):
        s+=arr[i]
        if s<=0:
            answer = "NO"
    s = 0
    for i in range(n-1, -1, -1):
        s += arr[i]
        if s <= 0:
            answer = "NO"
    print(answer)
#
# for _ in range(int(input())):
#     n=int(input())
#     l=list(map(int,input().split()))
#     q="YES"
#     su=0
#     print(l)
#     for i in range(n-1):
#         su+=l[i]
#         if su<=0:
#             q="NO"
#     su=0
#     for i in range(n-1,0,-1):
#         su+=l[i]
#         if su<=0:
#             q="NO"
#     print(q)