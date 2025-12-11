# https://leetcode.com/problems/max-consecutive-ones-iii/
# 1004-max-consecutive-ones-iii


# I think I can change every 0s that I encounter. (increase window size only if k >0 or encounter 1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_ones = 0
        for r, num in enumerate(nums):
            if num == 0:
                if k > 0:
                    k -= 1
                else:
                    while nums[l] == 1:
                        l += 1
                    l += 1
            max_ones = max(max_ones, r - l + 1)

        return max_ones
