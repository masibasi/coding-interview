# https://leetcode.com/problems/maximum-subarray/
# 53-maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sub_sum = 0
        max_sum = 0
        positive = False
        max_val = float("-inf")
        for num in nums:
            if num > 0:
                positive = True
            if sub_sum + num < 0:
                sub_sum = 0
            elif sub_sum + num >= 0:
                sub_sum += num
                if max_sum < sub_sum:
                    max_sum = sub_sum
            max_val = max(max_val, num)

        if positive == False:
            return max_val
        return max_sum


# Candanes'
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            # 현재 원소를 새로 시작할지, 기존 subarray에 이어붙일지 선택
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum
