#https://leetcode.com/problems/minimum-window-substring/
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        need = len(cnt_t)
        have = 0
        l, r = 0, 0
        d = defaultdict(int)
        lr = [-1, -1]
        minlen = float("inf")
        while r < len(s):
            if s[r] in cnt_t:
                d[s[r]] += 1
                if d[s[r]] == cnt_t[s[r]]:
                    have += 1

            while have == need:
                if r - l + 1 < minlen:
                    lr = [l, r]
                    minlen = r - l + 1
                if s[l] in cnt_t:
                    d[s[l]] -= 1
                    if d[s[l]] < cnt_t[s[l]]:
                        have -= 1
                l += 1
            r += 1
        return s[lr[0]:lr[1] + 1]