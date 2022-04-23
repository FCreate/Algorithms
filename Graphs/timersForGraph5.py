# simple dfs
visited = set()
timeIn = [0 for _ in range(n)]
timeOut = [0 for _ in range(n)]
dfsTimer = 0
color = [0 for _ in range(n)]


def dfs(g, v):
    color[v] = 1
    global dfsTimer
    timeIn[v] = dfsTimer
    dfsTimer += 1
    visited.add(v)
    for i in g[v]:
        if i not in visited:
            dfs(g, i)
    timeOut[v] = dfsTimer
    dfsTimer += 1
    color[v] = 2


def mainDFS(g):
    for i in range(n):
        if color[v] == 0:
            dfs(g, i)


order = []


def topSort(g, v):
    color[v] = 1
    for i in g[v]:
        if color[i] == 0:
            topSort(g, i)
    color[v] = 2
    order.append(v)


0 -> 1


def canFinish(numCourses, prerequisites):
    g = [[] for _ in range(numCourses)]
    for p in prerequisites:
        g[p[1]].append(p[0])
    color = [0 for _ in range(numCourses)]
    b = True

    def dfs(g, v):
        nonlocal b
        if color[v] == 1:
            b = False
        elif color[v] == 0:
            color[v] = 1
            for i in g[v]:
                if color[i] == 0:
                    dfs(g, i)
                elif color[i] == 1:
                    b = False
            color[v] = 2
            return True

    # cycle?
    for i in range(numCourses):
        if color[i] == 0:
            dfs(g, i)
            if not b:
                return False

    return True


0 ->? 1
1 -> 0


def canFinish(numCourses, prerequisites):
    g = [[] for _ in range(numCourses)]
    for p in prerequisites:
        g[p[1]].append(p[0])
    color = [0 for _ in range(numCourses)]

    def dfs(g, v):
        if color[v] == 1:
            return False
        if color[v] == 2:
            return True
        color[v] = 1
        for i in g[v]:
            if not dfs(g, i):
                return False
        color[v] = 2
        return True

    for i in range(numCourses):
        if not dfs(g, i):
            return False
    return True


g = [[] for _ in range(numCourses)]
for p in prerequisites:
    g[p[1]].append(p[0])
color = [0 for _ in range(numCourses)]
b = True


def dfs(g, v):
    nonlocal b
    color[v] = 1
    for i in g[v]:
        if color[i] == 0:
            dfs(g, i)
        elif color[i] == 1:
            b = False
    color[v] = 2
    self.resa.append(v)
    return True


# cycle?
for i in range(numCourses):
    if color[i] == 0:
        dfs(g, i)
        if not b:
            return False

return True

Input
2
[[0, 1]]
Output
false
Expected
true

