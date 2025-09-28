# https://leetcode.com/problems/product-of-array-except-self/
# 238-product-of-array-except-self

# Idea :
# 1. Brute Force :
## use nested loop except for the index to mult for the rest
## n^2

# 2. Optimized:
## What if I mult all together and divide each elem?
## -> in the desc, said to not use div.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        l, r = 1, 1
        mult = []
        for i in range(n):
            mult.append(l)
            l = l * nums[i]

        for i in range(n - 1, -1, -1):
            mult[i] = mult[i] * r
            r = nums[i] * r

        return mult
