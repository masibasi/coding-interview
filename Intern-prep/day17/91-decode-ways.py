# https://leetcode.com/problems/decode-ways/description/
# 91-decode-ways


class Solution:
    def numDecodings(self, s: str) -> int:
        if s and s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
        # dp = [1 for _ in range(len(s))]
        # dp[0] = 1

        # for i in range(1, len(s)):
        #     if int(s[i]) == 0:
        #         if int(s[i-1]) == 0:
        #             return 0
        #         else :
        #             dp[i] = dp[i-2]
        #             continue
        #     if 1 <= int(s[i-1:i+1]) <= 26:
        #         print(int(s[i-1:i+1]))
        #         if int(s[i-1]) == 0:
        #             dp[i] = dp[i-1]
        #         else :
        #             dp[i] = dp[i-1] + 1
        #     elif int(s[i-1:i+1]) > 26:
        #         dp[i] = dp[i-1]

        # print(dp)
        # return dp[-1]
