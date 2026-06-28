# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        ans = [1] * len(nums)
        for i, num in enumerate(nums):
            ans[i] = left * ans[i]
            left *= num
        # nums.reverse()
        # for i, num in enumerate(nums):
            # ans[len(nums) - 1 - i] = right * ans[len(nums) - 1 - i]
            # right *= num

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        

        return ans