#https://codeforces.com/contest/1366/problem/A?locale=ru
t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    print(min(a, b, (a+b)//3))

#O(n)
# t = int(input())
# for _ in range(t):
#     a, b = list(map(int, input().split()))
#     #print(f"{a}  {b}")
#     geme = 0
#     while a + b >=3 and (a >=2 or b>=2) and a > 0 and b > 0:
#         if a > b:
#             a-=2
#             b-=1
#         else:
#             b-=2
#             a-=1
#         geme += 1
#     print(geme)