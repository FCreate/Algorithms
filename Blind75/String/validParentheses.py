#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for elem in s:
            if elem in d:  # open bracket
                stack.append(elem)
            else:
                if len(stack) > 0 and d[stack.pop()] == elem:
                    pass
                else:
                    return False

        if len(stack) != 0:
            return False
        return True

