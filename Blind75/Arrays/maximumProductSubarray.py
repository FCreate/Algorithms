#https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        _max = nums[0]
        _min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                _max, _min = _min, _max
            _max = max(nums[i], _max*nums[i])
            _min = min(nums[i], _min*nums[i])
            maxProduct = max(maxProduct, _max)
        return maxProduct