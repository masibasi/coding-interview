# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0

        ans = nums[0]
        for num in nums:
            temp += num
            ans = max(ans, temp)
            if temp <0:
                temp = 0
        return ans