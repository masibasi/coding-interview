# https://leetcode.com/problems/house-robber/
# 198-house-robber

# Brute force
# - 모든 경우의 수를 본다면 O(2^n)에 근접해질것.

# DP
# - rob(n) = rob(n-2) + list[n] or rob(n-1)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # max_rob = [0] * len(nums)
        # max_rob[0] = nums[0]
        # max_rob[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     max_rob[i] = max(max_rob[i-2] + nums[i], max_rob[i-1])
        # print(max_rob)
        # return max_rob[len(nums) - 1]
        prev2, prev1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cur = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = cur

        return prev1
