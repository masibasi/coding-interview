# https://leetcode.com/problems/climbing-stairs/
# 70-climbing-stairs

# 1. Brute force
## n^2 where you can either climb 1 or 2 every step. compute all possible


# 2. DP
## compute the smaller for the bigger
## D(n) = D(n-1) + D(n-2)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        prev1 = 2
        prev2 = 1
        for _ in range(3, n + 1):
            prev1, prev2 = prev1 + prev2, prev1
        return prev1
