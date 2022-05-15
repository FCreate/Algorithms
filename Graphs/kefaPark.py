import sys
sys.setrecursionlimit(180000)
n, m = list(map(int, input().split()))
bad_vertices = [0] + list(map(int, input().split()))
g = [[] for i in range(n+1)]

for _ in range(n-1):
    i, j = list(map(int, input().split()))
    g[i].append(j)
    g[j].append(i)
res = 0
visited = [False] * (n+1)
# def dfs(i, cnt):
#     global res
#     visited[i] = True
#     tmp = 0
#     for j in g[i]:
#         if not visited[j]:
#             tmp += 1
#             if bad_vertices[i] == 0:
#                 dfs(j, 0)
#             else:
#                 if cnt+1>m:
#                     visited[j] = True
#                 else:
#                     dfs(j, cnt + 1)
#     #this is leaf
#     if tmp == 0:
#         cnt += bad_vertices[i]
#         if cnt <= m:
#             res += 1
stack = []
stack.append((1,0))
while len(stack):
    i, cnt  = stack.pop()
    visited[i] = True
    tmp = 0
    for j in g[i]:
        if not visited[j]:
            tmp += 1
            if bad_vertices[i] == 0:
                stack.append((j, 0))
            else:
                if cnt+1>m:
                    visited[j] = True
                else:
                    stack.append((j, cnt + 1))
    if tmp == 0:
        cnt += bad_vertices[i]
        if cnt <= m:
            res += 1
print(res)