# https://leetcode.com/problems/valid-anagram/
# Idea :
## 1. brute force.
## - use nested loop to check all pairs
## - use an array to check second string. if char is used, check it to True
## - when all chars are used in t, return false.
## 2. use hash set
## - check the length of strings. if not same, return false
## - use every char in string s as key, the frequency as value.
## - compare it wth string t.
## 3. Use Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # count_s = {}
        # count_t = {}
        # for char in s:
        #      count_s[char] = count_s.get(char, 0) + 1
        # for char in t:
        #      count_t[char] = count_t.get(char, 0) + 1
        # if count_t == count_s:
        #     return True
        # return False
        return Counter(s) == Counter(t)
