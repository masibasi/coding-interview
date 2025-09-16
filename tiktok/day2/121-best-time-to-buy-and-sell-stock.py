# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121-best-time-to-buy-and-sell-stock

# 1. Brute Force
## compare every possible pairs of buy and sell
## O(n)


# 2. Optimization
## store min and max profit
##
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float(inf)

        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)
        return max_profit
