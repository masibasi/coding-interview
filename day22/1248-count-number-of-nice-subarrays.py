# https://leetcode.com/problems/count-number-of-nice-subarrays/
# 1248-count-number-of-nice-subarrays
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = {0: 1}  # prefix = 0은 시작 전 한 번 존재
        ans = 0

        for num in nums:
            prefix += num % 2

            if prefix - k in count:
                ans += count[prefix - k]

            count[prefix] = count.get(prefix, 0) + 1
        return ans
