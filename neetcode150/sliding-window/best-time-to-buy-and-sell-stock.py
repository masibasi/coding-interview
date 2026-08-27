# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        ans = 0
        for price in prices:
            min_p = min(min_p, price)
            ans = max(price - min_p, ans)

        return ans