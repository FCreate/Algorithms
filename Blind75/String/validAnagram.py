#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for elem in s:
            d[elem] = d.get(elem, 0) + 1
        for elem in t:
            if elem not in d:
                return False
            else:
                d[elem] = d[elem] - 1
                if d[elem] < 0:
                    return False
        return True if sum(d.values()) == 0 else False