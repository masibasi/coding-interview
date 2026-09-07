# Ideas :
## 1. Brute force ?
## - I have no idea
## 2. Stack
## - use 1 stack obj.
## - push every opening bracket into stack
## - pop stack if corresponding bracket is found
## - if the bracket is different, return False
## - if the stack is not empty, return False
## - if the stack is empty, return true
## Edge cases :
## - if the next char is closing bracket but stack is empty, return False


# class Solution:
#     def isValid(self, s: str) -> bool:
#         bracket_stack = []
#         for bracket in s:
#             if bracket == '[' or bracket == '{' or bracket == '(':
#                 bracket_stack.append(bracket)
#             else :
#                 if len(bracket_stack) == 0:
#                     return False
#                 if bracket == ']':
#                     if bracket_stack.pop() == '[':
#                         continue
#                     else:
#                         return False
#                 elif bracket == '}':
#                     if bracket_stack.pop() == '{':
#                         continue
#                     else:
#                         return False
#                 elif bracket == ')':
#                     if bracket_stack.pop() == '(':
#                         continue
#                     else:
#                         return False

#         if len(bracket_stack) != 0:
#             return False
#         return True


# Optimized Clean version :
# - use hash map
# - iterate map using .values()

# class Solution:
# def isValid(self, s: str) -> bool:
#     stack = []
#     bracket_map = {')': '(', '}': '{', ']': '['}

#     for char in s:
#         if char in bracket_map.values():  # 여는 괄호
#             stack.append(char)
#         elif char in bracket_map:  # 닫는 괄호
#             if not stack or stack.pop() != bracket_map[char]:
#                 return False
#         else:
#             return False  # 유효하지 않은 문자 처리 (optional)

#     return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            if len(stack) == 0:
                return False
            if char == ")":
                if "(" != stack.pop():
                    return False
            if char == "]":
                if "[" != stack.pop():
                    return False
            if char == "}":
                if "{" != stack.pop():
                    return False
        if len(stack) != 0:
            return False
        return True
