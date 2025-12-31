# https://leetcode.com/problems/reverse-integer/
# 7-reverse-integer


class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        x = abs(x)

        ans = 0

        while x != 0:
            dig = x % 10
            x //= 10
            ans = ans * 10 + dig

        ans *= sign

        if not -(2**31) < ans < 2**31:
            return 0
        return ans
