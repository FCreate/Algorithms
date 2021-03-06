#https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return heapq.nlargest(k, cnt, key = lambda num:(cnt[num], num))