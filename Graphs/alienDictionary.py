#https://www.lintcode.com/problem/892/description
"""
Reformulate dictionary and use bfs + priority queue [ab, adc] -> abcd
"""
from typing import (
    List,
)


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        g = {c: set() for w in words for c in w}
        for i in range(1, len(words)):
            word1, word2 = list(words[i - 1]), list(words[i])
            minlen = min(len(word1), len(word2))
            if word1[:minlen] == word2[:minlen] and len(word1) > len(word2):
                return ""
            for j in range(minlen):
                if word1[j] != word2[j]:
                    g[word1[j]].add(word2[j])
                    break

        color = {}
        for c in g:
            color[c] = 0

        order = []
        isPossible = True

        def dfs(v):
            nonlocal isPossible
            if not isPossible:
                return
            color[v] = 1
            for i in g[v]:
                if color[i] == 0:
                    dfs(i)
                elif color[i] == 1:
                    isPossible = False
            color[v] = 2
            order.append(v)

        for c in sorted(g.keys(), reverse=True):
            if color[c] == 0:
                dfs(c)

        return "".join(order[::-1]) if isPossible else ""



from typing import (
    List,
)
from heapq import heapify, heappush, heappop

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        g = {c: set() for w in words for c in w}
        for i in range(1, len(words)):
            word1, word2 = list(words[i - 1]), list(words[i])
            minlen = min(len(word1), len(word2))
            if word1[:minlen] == word2[:minlen] and len(word1) > len(word2):
                return ""
            i = 0
            while i < len(word1) and i < len(word2):
                if word1[i] != word2[i]:
                    g[word1[i]].add(word2[i])
                    break
                i += 1
        n = len(g.keys())
        color = {}
        for c in g:
            color[c] = 0

        order = []
        isPossible = True
        indegree = {node : 0 for node in g}
        for node in g:
            for neighbor in g[node]:
                indegree[neighbor] += 1
        queue = [node for node in g if indegree[node] == 0]
        heapify(queue)

        # def dfs(v):
        #     nonlocal isPossible
        #     if not isPossible:
        #         return
        #     color[v] = 1
        #     for i in g[v]:
        #         if color[i] == 0:
        #             dfs(i)
        #         elif color[i] == 1:
        #             isPossible = False
        #     color[v] = 2
        #     order.append(v)
        #
        # while queue:
        #     c = heappop(queue)
        #     if color[c] == 0:
        #         dfs(c)

        topo_order = ""
        while queue:
            node = heappop(queue)
            topo_order += node
            for neighbor in g[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor)

        # if all nodes popped
        if len(topo_order) == len(g):
            return topo_order

        return ""


sol = Solution()
print(sol.alien_order(["wrt","wrf","er","ett","rftt"]))
#assert sol.alien_order(["wrt","wrf","er","ett","rftt"]) == "wertf"
print(sol.alien_order(["z","x"]))
# assert sol.alien_order(["z", "x"]) == "zx"
print(sol.alien_order(["ab","adc"]))
# assert sol.alien_order(["ab","adc"]) == "abcd"