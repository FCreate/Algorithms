#https://leetcode.com/problems/trapping-rain-water/ 
class Solution:
    def trap(self, height: List[int]) -> int:
        result, maxL, maxR, L, R = 0, height[0], height[-1], 0, len(height)-1
        while L < R:
            if maxL < maxR:
                L += 1
                maxL = max(maxL, height[L])
                result += max(0, maxL- height[L])
            else:
                R -= 1
                maxR = max(maxR, height[R])
                result += max(0, maxR - height[R])
        return result