# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3-longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)

        l = 0

        ans = 0
        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
                seen[char] = r
            else:
                seen[char] = r
                ans = max(ans, r - l + 1)

        return ans
