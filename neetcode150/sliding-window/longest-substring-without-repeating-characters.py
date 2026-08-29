# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        l = 0
        ans = 0
        for i, c in enumerate(s):
            if c in seen:
                while l <= seen[c]:
                    del seen[s[l]]
                    l += 1
            seen[c] = i
            ans = max(ans, i - l + 1)
        return ans