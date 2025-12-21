# https://leetcode.com/problems/subarray-product-less-than-k/
# 713-subarray-product-less-than-k
# helped by gpt
class Solution:
    # Time Limit
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return 0

        ans = 0

        for i in range(n):
            prod = nums[i]
            if prod < k:
                ans += 1
            else:
                continue
            for j in range(i + 1, n):
                prod *= nums[j]
                if prod < k:
                    ans += 1

        return ans

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k <= 1:
            return 0

        ans = 0
        l = 0
        prod = 1
        for r, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[l]
                l += 1
            ans += r - l + 1

        return ans
