# https://leetcode.com/problems/contiguous-array/
# 525-Contiguous-Array
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Brute Force
        max_len = 0
        for i in range(len(nums)):
            zero = 0
            one = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zero += 1
                if nums[j] == 1:
                    one += 1
                if zero == one:
                    max_len = max(max_len, j - i + 1)

        return max_len

    # Optimized
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        last_seen = {0: -1}

        max_len = 0
        for i, num in enumerate(nums):
            prefix += 1 if num == 1 else -1

            if prefix in last_seen:
                max_len = max(max_len, i - last_seen[prefix])
            else:
                last_seen[prefix] = i

        return max_len
