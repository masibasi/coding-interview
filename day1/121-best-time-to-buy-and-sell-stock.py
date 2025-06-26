# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Ideas:
# 1. Brute force
# I will iterate twice with a nested loop to find the biggest max - min. find the biggest possible profit while looking at all possible pairs.
# This is O(n2), since it has nested loop with a n of len(prices)
# 2. Sort?
# I will sort the input in ascending order. then, I will compare from each end to look for biggest available pair? <- Im not that sure so hold
# 3. One way scan solution
# scan for the min and max. if min appears after max, max is reset to min. if next num is greater than prev, compare with max. return max - min
# how to check min appear after max ? -> if min == max
# in this case, time complexity => O(n) with n == len(prices)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force
        # profit_max = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         buy = prices[i]
        #         sell = prices[j]
        #         profit = sell - buy
        #         if profit > profit_max:
        #             profit_max = profit
        # return profit_max
        # One way scan
        # profit = 0
        # max = -1
        # min = -1
        # for i in range(len(prices)):
        #     if prices[i] > max:
        #         if min == -1:
        #             min = prices[i]
        #         max = prices[i]
        #     if prices[i] < min:
        #         if min == max:
        #             max = prices[i]
        #         min = prices[i]
        # profit = max - min
        # return profit
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
