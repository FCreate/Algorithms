#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(res, self.helper(s, i, i), self.helper(s, i, i + 1), key = len)
        return res
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -=1; r += 1
        return s[l+1 : r]