#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        h = set()
        i, j, maxlen = 0, 0, 0
        while i < n and j < n:
            if s[j] not in h:
                h.add(s[j])
                j += 1
                maxlen = max(maxlen, j - i)
            else:
                h.remove(s[i])
                i += 1
        return maxlen
