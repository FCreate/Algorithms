#https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, reach, n = 0, 0, len(nums)
        while i < n and reach < n:
            if reach < i:
                return False
            reach = max(reach, i + nums[i])
            i += 1

        return reach >= n - 1
