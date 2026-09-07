# https://leetcode.com/problems/is-subsequence/
# 392-is-subsequence.py


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # I can do it with two pointers.

        # edge case :
        n, m = len(s), len(t)
        if n > m:
            return False
        if n == 0:
            return True

        i = 0
        for char in t:
            if s[i] == char:
                i += 1
            if i == n:
                return True

        return False
