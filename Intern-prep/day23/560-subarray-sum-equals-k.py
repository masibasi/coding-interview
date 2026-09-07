# https://leetcode.com/problems/subarray-sum-equals-k/
# 560-subarray-sum-equals-k


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        con_hash = defaultdict(int)
        ans = 0
        prefix_sum = 0
        # calculate all prefix, con_hash
        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum == k:
                ans += 1
            con = prefix_sum - k

            ans += con_hash[con]
            con_hash[prefix_sum] += 1
        return ans
