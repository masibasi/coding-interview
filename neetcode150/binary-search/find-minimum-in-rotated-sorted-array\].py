
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/\
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            mid = (l + r) // 2
            if nums[l] == nums[mid]:
                return min(nums[l], nums[r])
            elif nums[l] > nums[mid]:
                r = mid 
            elif nums[l] < nums[mid]:
                l = mid + 1
