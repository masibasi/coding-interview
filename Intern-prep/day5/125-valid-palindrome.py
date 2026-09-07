# https://leetcode.com/problems/valid-palindrome/
# 125-valid-palindrome


# Ideas
# 1. Naive
# - remove all non-alphanumerics
# - create another string, make it backwards
# 2. Little Optimization
# - ignore the non-alphas
# - use two pointers
# - if an alphanumeric char is selected, compare two.
# - stop if leftindex bigger than right
# - if len(str) == 1, return true.


# 기억할 것 : .isalnum()함수를 잘 써먹자!!
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned = ''.join(c.lower() for c in s if c.isalnum())
#         return cleaned == cleaned[::-1]
