class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # base case: 합이 0이 되는 경우는 아무것도 선택하지 않는 1가지 방법

        for total in range(1, target + 1):
            for num in nums:
                if total - num >= 0:
                    dp[total] += dp[total - num]

        return dp[target]
