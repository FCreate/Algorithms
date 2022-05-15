#https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =  list(filter(lambda x: x.isalpha() or x.isnumeric(), s.lower()))
        if s == s[::-1]:
            return True
        else:
            return False