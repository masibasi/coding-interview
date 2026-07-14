# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from ast import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isnumeric() or len(token) > 1:
                stack.append(token)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    stack.append(int(num1) + int(num2))
                elif token == "-":
                    stack.append(int(num2) - int(num1))
                elif token == "*":
                    stack.append(int(num1) * int(num2))
                elif token == "/":
                    stack.append(int(int(num2) / int(num1)))

        return int(stack[0])