# https://leetcode.com/problems/longest-repeating-character-replacement/description/
# 424-longest-repeating-character-replacement


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        ans = 0
        l = 0
        max_freq = 0
        for r, char in enumerate(s):
            frequency[char] += 1
            max_freq = max(max_freq, frequency[char])
            if r - l + 1 - max_freq > k:
                while (r - l + 1) - max_freq > k:
                    frequency[s[l]] -= 1
                    l += 1

            ans = max(ans, r - l + 1)

        return ans
