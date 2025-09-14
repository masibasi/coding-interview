# https://leetcode.com/problems/min-cost-climbing-stairs/
# 746-min-cost-climbing-stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        tot = [0] * len(cost)
        tot[0] = cost[0]
        tot[1] = cost[1]
        print(cost)
        for n in range(2, len(cost)):
            print(n)
            tot[n] = min(tot[n - 1] + cost[n], tot[n - 2] + cost[n])
        print(tot)

        return tot[-1]
