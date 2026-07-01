# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                opening_char = stack.pop()
                if not (opening_char == '[' and char == ']' or opening_char == '(' and char == ')' or opening_char == '{' and char == '}') :
                    return False
        if len(stack) != 0:
            return False
        return True

    def isValid(self, s: str) -> bool:
        mapping = {'}' : '{', ')' : '(', ']' : '['}
        stack = []
        for char in s:
            if char in mapping:
                if not stack:
                    return False
                if stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0