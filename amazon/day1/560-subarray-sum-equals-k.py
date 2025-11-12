# https://leetcode.com/problems/subarray-sum-equals-k/
# 560-subarray-sum-equals-k

# Brute force: N^2 : find all subarrays

# Idea:
# 'sequence'니까 투포인터?
# 포인터 하나 고정시키고 사이 값들이 k 미만일때 오른쪽 쭉 증가시키다 k 넘어가면 왼쪽 포인터 이동 시키면 되지 않을까
## 오류발생 -> negative numbers 에 대응하지 못함


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # ## Brute force
        # ans = 0
        # for i in range(n):
        #     sub_sum = 0
        #     for j in range(i, n):
        #         sub_sum += nums[j]
        #         if sub_sum == k:
        #             ans += 1

        ## GPT Idea : save prefix sum
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # 초기값: 합이 0인 경우 1번 (빈 배열 취급)
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_counts:
                count += prefix_counts[prefix_sum - k]

            prefix_counts[prefix_sum] += 1
        return count
