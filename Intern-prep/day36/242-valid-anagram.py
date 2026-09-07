# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        return counter_s == counter_t

    def isAnagram(self, s: str, t: str) -> bool:
        bucket_s = [0] * 26
        bucket_t = [0] * 26

        for char in s:
            index = ord(char.lower()) - ord("a")
            bucket_s[index] += 1
        for char in t:
            index = ord(char.lower()) - ord("a")
            bucket_t[index] += 1

        return bucket_s == bucket_t
