# https://leetcode.com/problems/contiguous-array/
# 525-contiguous-array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        cur_sum = 0
        prefix_sum = defaultdict(int)
        ans = 0
        prefix_sum[0] = -1
        for i, num in enumerate(nums):
            if num == 0:
                cur_sum -= 1
            else:
                cur_sum += 1

            if cur_sum in prefix_sum:
                ans = max(ans, i - prefix_sum[cur_sum])
            else:
                prefix_sum[cur_sum] = i

        print(prefix_sum)

        return ans


            