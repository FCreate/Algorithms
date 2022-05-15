#https://leetcode.com/problems/cheapest-flights-within-k-stops/
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = [float("inf")] * n
        d[src] = 0
        for i in range(k+1):
            tmp = d.copy()
            for flight in flights:
                f, to, p = flight
                if d[f] != float("inf") and d[f] + p < tmp[to]:
                    tmp[to] = d[f] + p
            d = tmp
        return d[dst] if d[dst] != float("inf") else -1