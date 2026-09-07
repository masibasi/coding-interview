# Idea:
## 1. Brute force:
## - I am going to turn the string s into an array
## - go thru a nested loop with array and t if the len of s & t is same
## - if i find a char, check the array and put true into the matching array
## - if all value of array is true at last, return true (length is same)
## - if a char is not found in array, return false
## 2. Optimize:
## - instead of arrays, use set {} for each strings
## - use char as key, and # of chars -> val
## - iterate each string, make each set.
## - campare the two sets.
## - Return false : * key from s not found in t
## * val from key in s different with t
## - else return true


## Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case? -> It is okay to use unicode characters as python key.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {}
        set_t = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in set_s:
                set_s[char] += 1
            else:
                set_s[char] = 1
        for char in t:
            if char in set_t:
                set_t[char] += 1
            else:
                set_t[char] = 1

        for key in set_s:
            if key in set_t:
                if set_s[key] != set_t[key]:
                    return False
            else:  # key not included
                return False
        return True
