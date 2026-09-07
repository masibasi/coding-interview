# https://leetcode.com/problems/word-break/description/
# 139-word-break

# 1. Brute Force :
## loop for the word Dict and s
## check the char pos that is found


# 2. DP
## dp[i] = s[0:i + 1] == s[0:i - len(word)] + word
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):  # s[0:i]까지 만들 수 있는가?
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)]:
                    if s[i - len(word) : i] == word:
                        dp[i] = True

        return dp[len(s)]
