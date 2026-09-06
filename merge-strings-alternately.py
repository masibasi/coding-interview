# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)

        ans = ''
        if n == m:
            for i in range(n):
                ans += word1[i] + word2[i]
        elif n > m:
            for i in range(m):
                ans += word1[i] + word2[i]
            ans += word1[m:]
        elif n < m:
            for i in range(n):
                ans += word1[i] + word2[i]
            ans += word2[n:]

        return ans