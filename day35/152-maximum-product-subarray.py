# https://leetcode.com/problems/maximum-product-subarray/
# 152-maximum-product-subarray


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = 0

        product = 1
        max_prod = float(-inf)
        num_neg = 0
        for r, num in enumerate(nums):
            if num == 0:
                while product < 0 and l < r:
                    product /= nums[l]
                    l += 1
                if l == r:
                    print("con", num)
                    l += 1
                    max_prod = max(max_prod, 0)
                    continue
                max_prod = max(max_prod, product)
                product = 1
                l = r + 1
                continue
            elif r == len(nums) - 1:
                product *= num
                while product < 0 and l < r:
                    product /= nums[l]
                    l += 1
            else:
                product *= num
            print("con2", num, l, r)
            max_prod = max(max_prod, product)

        return int(max_prod)
