# https://leetcode.com/problems/move-zeroes/
# 283-move-zeroes.py
# Ideas:
# - 1. Naive
## 2 for loops
## if 0 is found, switch with non-zero
## bad : 0(n2)

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 for j in range(i+1, len(nums)):
#                     if nums[j] != 0:
#                         nums[i] = nums[j]
#                         nums[j] = 0
#                         break


# 2. Two-pointer (O(n), in-place)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0
