# https://leetcode.com/problems/move-zeroes/
# 283-move-zeroes

# Brute force:
## n^2 

# Optimized - two pointers
## 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right, n in enumerate(nums):
            if n != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        
