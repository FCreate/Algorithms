#https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def helper(self, i):
        if self.visited[i] == 1:  # visited
            return False
        if self.visited[i] == 2:  # visited
            return True

        self.visited[i] = 1
        for elem in self.graph[i]:
            if not self.helper(elem):
                return False
        self.visited[i] = 2
        self.res.append(i)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = [[] for _ in range(numCourses)]

        for p in prerequisites:
            self.graph[p[0]].append(p[1])
        self.visited = [0] * numCourses
        self.res = []
        for i in range(len(self.graph)):
            if not self.helper(i):
                return []
        print(self.res)
        return self.res
