# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# 1658-minimum-operations-to-reduce-x-to-zero


class Solution:
    # Greedy : fail
    def minOperations(self, nums: List[int], x: int) -> int:

        l, r = 0, len(nums) - 1
        temp_sum = 0
        count = 0
        while l <= r:
            if temp_sum == x:
                return count
            if nums[l] + temp_sum > x and nums[r] + temp_sum > x:
                return -1

            if nums[l] + temp_sum > x:
                temp_sum += nums[r]
                r -= 1
            elif nums[r] + temp_sum > x:
                temp_sum += nums[l]
                l += 1
            elif nums[r] < nums[l]:
                temp_sum += nums[l]
                l += 1
            elif nums[l] <= nums[r]:
                temp_sum += nums[r]
                r -= 1
            count += 1
            if temp_sum == x:
                return count
        return -1

    # GPT solve
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        # target이 음수면 아예 불가능 (x가 전체 합보다 큰 경우)
        if target < 0:
            return -1
        # target == 0이면, 모든 원소를 다 빼야 함
        if target == 0:
            return len(nums)

        n = len(nums)
        l = 0
        cur_sum = 0
        max_len = -1

        for r, num in enumerate(nums):
            cur_sum += num

            while l <= r and cur_sum > target:
                cur_sum -= nums[l]
                l += 1

            if cur_sum == target:
                max_len = max(max_len, r - l + 1)

        if max_len == -1:
            return -1

        return n - max_len
