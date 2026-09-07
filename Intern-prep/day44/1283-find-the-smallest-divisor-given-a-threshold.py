# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_num = max(nums)

        smallest_thresh = float("inf")
        left, right = 1, max(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            total = 0
            for num in nums:
                total += math.ceil(num / mid)
            if total <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
