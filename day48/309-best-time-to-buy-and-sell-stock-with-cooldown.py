# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        buy = [0] * (n)
        sell = [0] * (n)
        cool = [0] * (n)

        buy[0] = -prices[0]

        for i in range(1, len(prices)):
            cool[i] = max(cool[i-1], sell[i-1])
            buy[i] = max(buy[i-1], cool[i-1] - prices[i])
            sell[i] = buy[i-1] + prices[i]

        return max(cool[n-1], sell[n-1])