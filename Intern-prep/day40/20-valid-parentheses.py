# https://leetcode.com/problems/valid-parentheses/
# 20-valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        op = ["(", "{", "["]
        cl = [")", "}", "]"]

        for char in s:
            if char in op:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                bracket = stack.pop()
                if bracket == "(" and not char == ")":
                    return False
                elif bracket == "{" and not char == "}":
                    return False
                elif bracket == "[" and not char == "]":
                    return False

        if stack:
            return False
        return True
