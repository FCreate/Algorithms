#https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_nums = len(nums)
        sum_nums = 0
        for idx in range(max_nums + 1):
            sum_nums += idx
        return sum_nums - sum(nums)