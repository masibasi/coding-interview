# https://leetcode.com/problems/binary-search/
# 704-binary-search

# 1. Brute force :
## search linearly, O(n)
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         for i, n in enumerate(nums):
#             if target == n:
#                 return i
#         return -1


# 2. Binary Search
## search the middle index. (left, right pointer)
## if target small, search left and right for big
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
