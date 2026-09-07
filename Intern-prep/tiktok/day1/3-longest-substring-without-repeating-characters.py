# https://leetcode.com/problems/two-sum/
# 1-two-sum

# Idea:
# 1. Brute force
## compare every pair with nested loop (n^2)


# 2. Optimized
## while checking the num, store the complement (target - now) into a hash map.
## I will store the complement as key and now as value
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            if num in store:
                return [i, store[num]]
            comp = target - num
            store[comp] = i


w
