class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def solve(n):
            if n in memo:
                return memo[n]
            if n == 0 or n == 1:
                return 1
            ans = 0
            for i in range(1, n + 1):
                ans += solve(i - 1) * solve(n - i)
            memo[n] = ans
            return ans
        return solve(n)