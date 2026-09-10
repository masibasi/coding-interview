# https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        max_len = 0
        freq = defaultdict(int)
        for i, char in enumerate(s):
            cur_len = i-l+1
            freq[char] += 1
            max_freq = max(max_freq, freq[char])
            if max_freq + k < cur_len:
                freq[s[l]] -=1
                l += 1
            max_len = max(max_len, i-l+1)

        return max_len
