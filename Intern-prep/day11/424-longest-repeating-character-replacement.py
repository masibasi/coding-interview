# https://leetcode.com/problems/longest-repeating-character-replacement/
# 424-longest-repeating-character-replacement

# idea:
# 모든 char 마다 순차적으로 바꿨을때, 안바꿨을 때 경욷의 가짓수가 있으니 brute force로 하면 2^n임.
# 이거는 점화식으로 풀어야할거같음
# 바꾸면 k를 썼을 때, 안 썼을 때가 나뉘니까 튜플의 형태로 최대 길이를 저장하면 어떨까?


# 이게 아니라 슬라이딩 윈도우문제였음.
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)  # 윈도우 내 각 문자 빈도
        left = 0
        max_freq = 0  # 윈도우 내 최빈도
        ans = 0

        for right, ch in enumerate(s):
            count[ch] += 1
            max_freq = max(max_freq, count[ch])

            # 필요 교체 수 = 윈도우 길이 - 최빈도
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1  # 윈도우 축소

            ans = max(ans, right - left + 1)

        return ans
