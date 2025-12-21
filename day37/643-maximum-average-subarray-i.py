# https://leetcode.com/problems/maximum-average-subarray-i/
# 643-maximum-average-subarray-i


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_avg = float("-inf")
        for i in range(k - 1, n):
            tempsum = 0
            for j in range(k):
                tempsum += nums[i - j]
            max_avg = max(max_avg, tempsum / k)

        return max_avg

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_avg = float("-inf")
        l = 0
        temp_sum = 0
        for r, num in enumerate(nums):
            if r - l + 1 <= k:
                temp_sum += num
            elif r - l + 1 > k:
                temp_sum += num
                temp_sum -= nums[l]
                l += 1
            if r - l + 1 == k:
                max_avg = max(max_avg, temp_sum)

        return max_avg / k
