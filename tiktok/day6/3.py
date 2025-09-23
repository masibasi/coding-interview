# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3-longest-substring-without-repeating-characters

# 아이디어
## 투 포인터 + 세트
## 만약 이미 본 캐릭터면 왼쪽 포인터 증가


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left = 0
        max_len = 0
        seen = set()
        for right, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left += 1
            seen.add(c)
            max_len = max(right - left + 1, max_len)

        return max_len
