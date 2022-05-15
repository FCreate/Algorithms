#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = currSum
        for i in range(1, len(nums)):
            if nums[i] + currSum > nums[i]:
                currSum = currSum + nums[i]
            else:
                currSum = nums[i]
            if currSum > maxSum:
                maxSum = currSum
        return maxSum