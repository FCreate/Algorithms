#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = 10**6
        for elem in prices:
            if elem - minprice > maxprofit:
                maxprofit = elem - minprice
            elif minprice > elem:
                minprice = elem
        return maxprofit