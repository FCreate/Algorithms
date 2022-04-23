#https://leetcode.com/problems/min-cost-to-connect-all-points/
class Solution:
    import heapq

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(point1, point2):
            return (abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))
        n = len(points)
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                d = distance(points[i], points[j])
                g[i].append((j, d))
                g[j].append((i, d))
        visited = set()
        visited.add(0)
        h = [] # [dist, i]
        for point in g[0]:
            heapq.heappush(h, (point[1], point[0])) #dist i"
        cost = 0
        add_elem = []
        while len(visited) < n:
            elem = heapq.heappop(h)
            while elem[1] in visited:
                elem = heapq.heappop(h)
            cost += elem[0]
            visited.add(elem[1])
            add_elem.append(elem[1])
            for point in g[elem[1]]:
                if point[0] not in visited:
                    heapq.heappush(h, (point[1], point[0]))
        return cost
