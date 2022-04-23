#https://leetcode.com/problems/network-delay-time/
#https://e-maxx.ru/algo/dijkstra
#https://e-maxx.ru/algo/dijkstra_sparse
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dists = {}
        g = [[] for _ in range(n + 1)]
        for i, j, t in times:
            g[i].append((j, t))
        h = [(0, k)]
        while h:
            d, i = heapq.heappop(h)
            if i not in dists:
                dists[i] = d
                for j, wj in g[i]:
                    heapq.heappush(h, (d + wj, j))

        return max(dists.values()) if len(dists) == n else -1