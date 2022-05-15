#https://codeforces.com/contest/796/problem/D
import sys
input = sys.stdin.readline
from collections import deque
n, k, d = list(map(int, input().split()))
police = list(map(int, input().split()))
g = [[] for _ in range(n+1)]
edges = {}
c = 1
for m in range(n-1):
    i, j = list(map(int, input().split()))
    g[i].append((j, m+1))
    g[j].append((i, m+1))
    c += 1
#print(c)
q = deque()
visited = [False] * (n+1)

for elem in police:
    q.append(elem)
    visited[elem] = True

#print(q)
visited_edges = [False] * (c)
res = 0
while q:
    i = q.popleft()
    for j, num_road in g[i]:
        if not visited[j]:
            visited[j] = True
            #visited_edges[edges[(min(i,j), max(i, j))]] = True
            if not visited_edges[num_road]:
                res += 1
                visited_edges[num_road] = True
            #print(edges[(min(i,j), max(i, j))])
            q.append(j)
print(n - 1 - res)
for i in range(1, c):
    if not visited_edges[i]:
        print(i, end = ' ')
