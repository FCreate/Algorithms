#https://leetcode.com/problems/swim-in-rising-water/
class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        visited = set((0,0))
        h = []
        heapq.heappush(h, (grid[0][0], 0, 0))
        max_height = 0
        while len(h) != 0:
            height, i, j = heapq.heappop(h)
            max_height = max(height, max_height)
            if i == (n-1) and j == (n-1):
                return max_height
            for add_i, add_j  in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                if (i + add_i) >=0 and (i + add_i) < n and (j + add_j) >= 0 and (j + add_j) < n and (i+add_i, j+add_j) not in visited:
                    visited.add((i+add_i, j+add_j))
                    heapq.heappush(h,(grid[i+add_i][j+add_j], i+add_i, j+add_j))