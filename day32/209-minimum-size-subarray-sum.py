# https://leetcode.com/problems/minimum-size-subarray-sum/
# 209-minimum-size-subarray-sum


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        sub_sum = 0
        l = 0
        min_size = float("inf")

        for r, num in enumerate(nums):
            sub_sum += num

            while sub_sum >= target:
                min_size = min(min_size, r - l + 1)
                sub_sum -= nums[l]
                l += 1

        return min_size if min_size != float("inf") else 0
