# https://leetcode.com/problems/coin-change-ii/
# 518-coin-change-ii


# Use DP
## for every money range, calc dp
## dp[n] += dp[n - coin]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
