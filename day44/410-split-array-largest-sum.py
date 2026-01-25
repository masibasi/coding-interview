# https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        low, high = max(nums), sum(nums)

        def can_split(max_sum):
            cur_sum = 0
            chunk = 1
            for num in nums:
                if cur_sum + num > max_sum:
                    chunk += 1
                    cur_sum = num
                else:
                    cur_sum += num
            return chunk <= k 

        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_split(mid):
                ans = mid
                high = mid -1
            else:
                low = mid + 1

        return ans