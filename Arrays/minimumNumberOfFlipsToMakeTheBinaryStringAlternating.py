#https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        one_first = '10' * n
        zero_first = '01' * n
        diff1, diff2 = 0, 0
        res = n
        l = 0
        for r in range(len(s)):
            if s[r] != one_first[r]:
                diff1 += 1
            if s[r] != zero_first[r]:
                diff2 += 1

            if r - l + 1 > n:
                if s[l] != one_first[l]:
                    diff1 -= 1
                if s[l] != zero_first[l]:
                    diff2 -= 1
                l += 1

            if r - l + 1 == n:
                res = min(res, diff1, diff2)

        return res