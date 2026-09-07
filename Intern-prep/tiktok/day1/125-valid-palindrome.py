# https://leetcode.com/problems/valid-palindrome/
# 125-valid-palindrome

# 1. Brute Force
## use another reversed string. replace all chars and cleanup.
## compare the both strings

# 2. Optimized
# compare from front and back


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
                continue
            else:
                return False
        return True
