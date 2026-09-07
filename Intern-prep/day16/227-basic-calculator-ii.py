# https://leetcode.com/problems/basic-calculator-ii/
# 227-basic-calculator-ii
# 지피티가 풀었는데 생각이 잘 안나네


class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip().replace(" ", "")
        stack = []
        num = 0
        sign = "+"
        n = len(s)

        for i in range(n):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)

            # 연산자이거나 마지막 문자일 때 처리
            if char in "+-*/" or i == n - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    prev = stack.pop()
                    stack.append(prev * num)
                elif sign == "/":
                    prev = stack.pop()
                    # 파이썬에서 정수 나눗셈은 음수 처리가 다르므로 다음과 같이 처리
                    stack.append(int(prev / num))
                sign = char
                num = 0

        return sum(stack)
