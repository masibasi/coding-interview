# https://leetcode.com/problems/palindromic-substrings/
# 647-palindromic-substrings

# GPT Helped


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        pal = 0

        def expand(l, r):
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l += -1
                r += 1
            return cnt

        for i in range(n):
            pal += expand(i, i)
            pal += expand(i, i + 1)
        return pal
