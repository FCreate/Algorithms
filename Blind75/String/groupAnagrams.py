#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            tmp = tuple(sorted(word))
            d[tmp] = d.get(tmp, []) + [word]
        return d.values()