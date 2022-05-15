#https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        first = 1
        second = 2
        for i in range(3, n + 1):
            tmp = second
            second = first + second
            first = tmp
        return second