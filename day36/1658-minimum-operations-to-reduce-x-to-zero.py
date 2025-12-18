# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# 1658-minimum-operations-to-reduce-x-to-zero


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_nums = sum(nums)
        target = sum_nums - x
        if target < 0:
            return -1

        l = 0
        window_sum = 0
        max_window = -1
        for r, num in enumerate(nums):
            window_sum += num
            while window_sum > target:
                window_sum -= nums[l]
                l += 1
            if window_sum == target:
                max_window = max(max_window, r - l + 1)

        return len(nums) - max_window if max_window != -1 else -1
