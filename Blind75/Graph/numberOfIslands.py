#https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c = 0
        n, m = len(grid), len(grid[0])
        def dfs(i,j):
            nonlocal n
            nonlocal m
            dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
            for d in dirs:
                new_i = d[0] + i
                new_j = d[1] + j
                if new_i < n and new_i >=0 and new_j < m and new_j >= 0 and grid[new_i][new_j] == "1":
                    grid[new_i][new_j] = "0"
                    dfs(new_i, new_j)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    c += 1
                    dfs(i,j)
        return c