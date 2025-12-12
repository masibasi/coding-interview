# https://leetcode.com/problems/3sum-closest/submissions/1853597904/
# 16-3sum-closet
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Brute Force : Three pointers -> Time Limit E
        n = len(nums)
        min_diff = float("inf")
        for i in range(n - 2):
            tar_i = target - nums[i]
            for j in range(i + 1, n - 1):
                tar_i_j = tar_i - nums[j]
                for k in range(j + 1, n):
                    tar_i_j_k = tar_i_j - nums[k]
                    # print(tar_i_j_k, nums[k])
                    if abs(tar_i_j_k) < min_diff:
                        min_diff = abs(tar_i_j_k)
                        ans = nums[i] + nums[j] + nums[k]
        return ans

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        min_diff = float("inf")
        ans = 0
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                sub_sum = nums[i] + nums[l] + nums[r]
                if abs(target - sub_sum) < min_diff:
                    min_diff = abs(target - sub_sum)
                    ans = sub_sum
                if sub_sum < target:
                    l += 1
                else:
                    r -= 1
        return ans
