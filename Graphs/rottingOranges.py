#https://leetcode.com/problems/rotting-oranges/
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rotten = deque()
        number_rotten = 0
        t = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append((i, j, t))
                elif grid[i][j] == 1:
                    number_rotten += 1

        while rotten:
            i, j, t = rotten.popleft()
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for add_i, add_j in dirs:
                new_i = i + add_i
                new_j = j + add_j
                if 0 <= new_i and new_i < n and 0 <= new_j and new_j < m and grid[new_i][new_j] == 1:
                    grid[new_i][new_j] = 2
                    rotten.append((new_i, new_j, t + 1))
                    number_rotten -= 1

        if number_rotten > 0:
            return -1
        else:
            return t