def numberOfConnectedComponentsWithoutTrace(n, edges):
    g = [[] for _ in range(n)]
    for e in edges:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    visited = set()
    connectedComponents = 0
    def dfs(i):
        visited.add(i)
        for elem in g[i]:
            if elem not in visited:
                dfs(elem)

    for i in range(n):
        if i not in visited:
            dfs(i)
            connectedComponents+=1

    return connectedComponents
print(numberOfConnectedComponentsWithoutTrace(5, [[0, 1], [1, 2], [3,4]]))
print(numberOfConnectedComponentsWithoutTrace(5, [[0, 1], [1, 2], [2,3], [3,4]]))

def numberOfConnectedComponents(n, edges):
    g = [[] for _ in range(n)]
    for e in edges:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
    visited = set()
    connectedComponents = []
    def dfs(i, tmp):
        visited.add(i)
        tmp.append(i)
        for elem in g[i]:
            if elem not in visited:
                tmp = dfs(elem, tmp)
        return tmp

    for i in range(n):
        if i not in visited:
            connectedComponents.append(dfs(i, []))
    return connectedComponents
