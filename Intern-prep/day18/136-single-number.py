# https://leetcode.com/problems/single-number/
# 136-single-number

# Brute Force


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1

        for num in nums:
            if seen[num] == 1:
                return num


# sort
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[len(nums) - 1]


# XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # 하나씩 XOR
        return result
