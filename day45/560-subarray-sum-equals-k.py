# https://leetcode.com/problems/subarray-sum-equals-k/
# 560-subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Prefix sum

        left_sum = defaultdict(int)
        cur_sum = 0
        ans = 0
        left_sum[0] = 1

        for num in nums:
            cur_sum += num
            need = cur_sum - k
            ans += left_sum[need]
            left_sum[cur_sum] += 1

        return ans