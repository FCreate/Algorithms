#https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        need = [0] +[amount + 1] * amount
        for a in range(min(coins), amount + 1):
            need[a] = min([need[a-c] for c in coins if c <= a]) + 1
        return need[-1] if need[-1] <= amount else -1