# https://leetcode.com/problems/valid-parentheses/
# 20-valid-parentheses

# 1. Brute Force:
## ----

# 2. use Stack
## first need to close the recent opened bracket -> stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for br in s:
            if br in brackets:
                stack.append(br)
            else:
                if not stack:
                    return False
                cur = stack.pop()
                if brackets[cur] != br:
                    return False
        return True if not stack else False
