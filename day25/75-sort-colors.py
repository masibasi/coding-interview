# https://leetcode.com/problems/sort-colors/
# 75-sort-colors


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute force:
        # count all.
        n = len(nums)
        count = Counter(nums)
        i = 0
        while i < n:
            while count[0] > 0:
                nums[i] = 0
                count[0] -= 1
                i += 1
            while count[1] > 0:
                nums[i] = 1
                count[1] -= 1
                i += 1
            while count[2] > 0:
                nums[i] = 2
                count[2] -= 1
                i += 1

    # Intuitive ver:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low, mid, high = 0, 0, n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
