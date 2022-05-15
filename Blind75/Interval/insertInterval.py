#https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left = [elem for elem in intervals if elem[1] < s]
        right = [elem for elem in intervals if elem[0] > e]
        if len(left) + len(right) != len(intervals):
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][1])
        return left + [[s, e]] + right