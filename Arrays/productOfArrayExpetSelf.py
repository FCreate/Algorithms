#https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        p = 1
        for i in range(1, n):
            p*=nums[i-1]
            prefix[i] = p
        suffix = [1] * n
        p = 1
        for i in range(n-1, 0, -1):
            p*= nums[i]
            suffix[n - i] = p
        res = [0] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[n - i - 1]
        return res