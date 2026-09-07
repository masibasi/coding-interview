# https://leetcode.com/problems/running-sum-of-1d-array/description/
# Ideas :
## 1. Naive Solution
## - loop up to i every time to add up.
## - time : O(n2) ??
## 2. Optimized
## - add every i with sum[i-1]
## 5mins
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = []
        for i, num in enumerate(nums):
            if i == 0:
                sum.append(num)
            else:
                sum.append(sum[i - 1] + num)

        return sum
