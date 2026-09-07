# https://leetcode.com/problems/maximum-subarray/
## [ Time taken: 41 m 22 s ]
# Ideas :
## 1. Brute force : compare all possible sub arrays... that would be too big
## 2. Optimized :
## - compare digits from start.
## - need two pointers (start, end)
## - if positive, add sum
## - if negative and it makes sum < 0, move pointer to next.
## - if negative, check next & create temp sum
## - - if next is positive, compare temp sum with sum.
## - - if temp sum is bigger, move end pointer
## - i think this is not a good direction... i shall get some help
## 3. Kadane’s Algorithm (greedy)
## - if subarray is neg, restart.
## - record the maximum sum
## - edge cases : if only num is neg, if all nums are negative, all is 0


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp_sum = 0
        max_sum = 0
        all_neg_flag = True

        for num in nums:
            if temp_sum + num < 0:
                temp_sum = 0
                continue
            temp_sum += num
            if max_sum < temp_sum:
                max_sum = temp_sum
                all_neg_flag = False

        if all_neg_flag:  # can also handle all zeros
            return max(nums)
        return max_sum
