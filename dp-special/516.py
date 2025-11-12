# https://leetcode.com/problems/longest-palindromic-subsequence/

# dp[i][j] = max palindromic subsequence from i to j index

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        # basecase:
        for i in range(n):
            for j in range(n):
                if i==j:
                    dp[i+1][j+1] = 1


        for i in range(n, 0, -1):
            for j in range(i, n+1):
                if s[i-1] == s[j-1] and i != j:
                    dp[i][j] = dp[i+1][j-1] + 2
                elif i != j:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[1][n]
        