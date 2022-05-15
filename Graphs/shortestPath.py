import sys
input = sys.stdin.readline
from collections import deque
n, m, k = list(map(int, input().split()))
g = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = list(map(int, input().split()))
    g[i].append(j)
    g[j].append(i)
bad_seq = set()
for _ in range(k):
    i, j, k = list(map(int, input().split()))
    bad_seq.add((i,j,k))
visited_edges = set()
q = deque()
q.append([1, [-1]])
output = [-1]
while q:
    j, path = q.popleft()
    if j == n:
        output = path[1:] + [j]
        break
    for elem in g[j]:
        if (j, elem) not in visited_edges:
            if (path[-1], j, elem) not in bad_seq:
                visited_edges.add((j, elem))
                q.append((elem, path + [j]))
if len(output) > 1:
    print(len(output)-1)
    print(*output)
else:
    print(-1)