# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        ans = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            ans += prefix[cur_sum - k]
            prefix[cur_sum] += 1
        return ans
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
        
#         def helper(subarray, cur_sum):
#             temp = 0
#             for num in subarray:
#                 cur_sum += num
#                 if cur_sum == k:
#                     temp += 1
#             return temp
#         ans = 0
#         for i in range(len(nums)):
#             if nums[i] == k:
#                 ans += 1
#             ans += helper(nums[i+1:], nums[i])
#         return ans
# # class Solution:
# #     def subarraySum(self, nums: List[int], k: int) -> int:
# #         def dfs(subarray, cur_tot):
# #             if cur_tot == k:
# #                 return 1
# #             temp = 0
# #             for i in range(len(subarray)):
# #                 if i + cur_tot <= k:
# #                     temp += dfs(subarray[i+1:], cur_tot + subarray[i])
# #             return temp
        
# #         ans = 0
# #         for i in range(len(nums)):
# #             if nums[i] <= k:
# #                 ans += dfs(nums[i+1:], nums[i])

# #         return ans