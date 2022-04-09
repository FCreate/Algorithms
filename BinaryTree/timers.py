#Looking 
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
q = []
for _ in range(m):
    q.append(list(map(int, input().split())))
tree = [[] for _ in range(n + 1)]
root = None
for idx, elem in enumerate(arr):
    if elem == 0:
        root = idx + 1
    else:
        tree[elem].append(idx + 1)

timerIn = [0] * (n + 1)
timerOut = [0] * (n + 1)
used = set()
dfsTimer = 0


def dfs(v):
    global dfsTimer
    dfsTimer += 1
    timerIn[v] = dfsTimer
    used.add(v)
    for i in tree[v]:
        if i not in used:
            dfs(i)
    dfsTimer += 1
    timerOut[v] = dfsTimer


dfs(root)
for query in q:
    if timerOut[query[0]] > timerOut[query[1]] and timerIn[query[0]] < timerIn[query[1]]:
        print(1)
    else:
        print(0)
