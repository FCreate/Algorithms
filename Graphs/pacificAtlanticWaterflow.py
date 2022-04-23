#https://leetcode.com/problems/pacific-atlantic-water-flow/
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        # prim's style
        visited_pacific, visited_atlantic = set(), set()

        def dfs(i, j, s):
            s.add((i, j))
            dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
            for d in dirs:
                add_i, add_j = d[0], d[1]
                i_new = i + add_i
                j_new = j + add_j
                if i_new >= 0 and i_new < m and j_new >= 0 and j_new < n and (i_new, j_new) not in s and heights[i_new][
                    j_new] >= heights[i][j]:
                    dfs(i + add_i, j + add_j, s)

        # m - left and right borders
        for i in range(m):
            dfs(i, 0, visited_pacific)
            dfs(i, n - 1, visited_atlantic)
        # n - up and right borders
        for i in range(n):
            dfs(0, i, visited_pacific)
            dfs(m - 1, i, visited_atlantic)
        return list(visited_pacific.intersection(visited_atlantic))