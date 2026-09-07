# https://leetcode.com/problems/valid-anagram/
# 242-valid-anagram

# ideas
# 1. Brute force
## do a while nested loop for all s and t.
## store a check array for checking all s in t
## if all chars are checked for s and t len(s==t), return true
## else return false
## time comp (n^2) storage (n)


# 2. Hash set
## store all s into a hash set, value is freq for char
## if this two set is same for all chars, return true
## time comp (n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import Counter
        # return Counter(s) == Counter(t)
        set_s, set_t = {}, {}
        if len(s) != len(t):
            return False
        for char in s:
            # set_s[char] = 0 if char not in set_s else set_s[char] + 1
            set_s[char] = set_s.get(char, 0) + 1
        for char in t:
            # set_t[char] = 0 if char not in set_t else set_t[char] + 1
            set_t[char] = set_t.get(char, 0) + 1

        for char in set_s:
            if char in set_t:
                if set_s[char] != set_t[char]:
                    return False
            else:
                return False
        return True
