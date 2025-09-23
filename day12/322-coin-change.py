# https://leetcode.com/problems/coin-change/
# 322-coin-change

# greedy 하게 풀면 될거같은데?
# 그리디는 안되는구나


# DP로 해야겠다
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
