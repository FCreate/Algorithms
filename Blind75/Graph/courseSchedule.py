#https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            return True
        #cycle?
        for i in range(numCourses):
            if color[i] == 0:
                dfs(g,i)
                if not b:
                    return False

        return True
