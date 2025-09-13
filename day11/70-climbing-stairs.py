# https://leetcode.com/problems/climbing-stairs/
# 70-climbing-stairs

# Idea:
# 1.  Brute force :
# - 매 step마다 1혹은2로 해서 경우의 수를 모두 찾는다.
# - 매우 time consuming O(2^n).

# 2. Greedy
# - 2로 먼저 꽉 채워보고 이후 2대신 하나씩 1 집어넣어보기..??
# - 1을 집어넣을수록 경우의수가 많아질거같다


# 3. DP (Bottom up)
# - 1번쨰까지 경우의 수, 2번째까지 경우의 수, 등등 더하면 됨
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
