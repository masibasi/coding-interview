# https://leetcode.com/problems/binary-search/
# Idea :
## 1. Brute force : iterate thru all integers -> O(n)
## 2. Binary Search :
## - search the middle.
## - if found, return i
## - if middle < target , search the middle of upper half
## - if middle > target, search the lower half
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i, num in enumerate(nums):
        #     if num == target:
        #         return i
        # return -1
        # def binary_search(nums: List[int], target: int, start: int, end: int):
        #     if start > end:
        #         return -1
        #     middle = (start + end) // 2
        #     if target == nums[middle]:
        #         return middle
        #     elif target > nums[middle]:
        #         return binary_search(nums, target, middle + 1, end)
        #     elif target < nums[middle]:
        #         return binary_search(nums, target, start, middle - 1)
        # return binary_search(nums, target, 0, len(nums) - 1)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
