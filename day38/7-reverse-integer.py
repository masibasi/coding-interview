# https://leetcode.com/problems/valid-parentheses/
# 20-valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_list = ["(", "[", "{"]
        close_list = [")", "]", "}"]
        pair = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in open_list:
                stack.append(char)
            elif char in close_list:
                if not stack:
                    return False
                if pair[stack.pop()] != char:
                    return False

        if len(stack) == 0:
            return True
        return False
