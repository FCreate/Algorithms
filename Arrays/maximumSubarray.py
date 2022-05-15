#https://leetcode.com/problems/maximum-subarray/submissions/
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

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         currentSum = nums[0]
#         maxSum = nums[0]
#         for elem in nums[1:]:
#             currentSum = max(currentSum + elem, elem)
#             maxSum = max(currentSum, maxSum)
#             return maxSum
