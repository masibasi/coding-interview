# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        cur_sum = 0
        ans = 0
        prefix_sum[0] = 1
        for num in nums:
            cur_sum += num
            remainder = cur_sum % k
            if remainder in prefix_sum:
                ans += prefix_sum[remainder]
            prefix_sum[remainder] += 1

        return ans