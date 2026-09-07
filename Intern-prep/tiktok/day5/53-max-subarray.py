# https://leetcode.com/problems/maximum-subarray/
# 53-max-subarray

# IDEA
# 1. Brute force :
## 1크기 ~ n크기 윈도우로 모든 경우의 수 가운데 가장 큰걸 선택하는 것.
## O(n^2), time limit exceed

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = float("-inf")
#         for i in range(len(nums)): # 시작점
#             sub_sum = 0
#             for j in range(i, len(nums)): # 끝까지 모든 subarray랑 비교
#                 sub_sum += nums[j]
#                 max_sum = max(sub_sum, max_sum)
#         return max_sum

# 2. Optimization
## 순회하면서 음수가 된다면 무조건 현재 부분합을 0으로 초기화하는게 좋을듯

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(cur_sum, max_sum)

            if cur_sum < 0:
                cur_sum = 0

        return max_sum



#  If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         def helper(l, r):
#             if l == r:
#                 return nums[l]

#             mid = (l + r) // 2
#             left_max = helper(l, mid)
#             right_max = helper(mid + 1, r)

#             # cross sum
#             left_sum = float('-inf')
#             temp = 0
#             for i in range(mid, l - 1, -1):
#                 temp += nums[i]
#                 left_sum = max(left_sum, temp)

#             right_sum = float('-inf')
#             temp = 0
#             for i in range(mid + 1, r + 1):
#                 temp += nums[i]
#                 right_sum = max(right_sum, temp)

#             cross_sum = left_sum + right_sum

#             return max(left_max, right_max, cross_sum)

#         return helper(0, len(nums) - 1)