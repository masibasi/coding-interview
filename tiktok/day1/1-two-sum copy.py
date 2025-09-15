# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3-longest-substring-without-repeating-characters

# Idea:
# 1. Brute force
## Compare all possible substrings:
## time comp (2^n)

# 2. Sliding Window
## left pointer and right pointer.
## store the seen chars into a hash set, saving last index found
## if dup char is seen, move left pointer to the last found + 1 index


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        ans = 0

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            ans = max(ans, right - left + 1)
        return ans

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     left = 0
    #     seen = {}
    #     ans = 0

    #     for right, char in enumerate(s):
    #         if char in seen and seen[char] >= left:
    #             left = seen[char] + 1
    #         seen[char] = right
    #         ans = max(ans, right - left + 1)
    #     return ans
