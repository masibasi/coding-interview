# Ideas:
## 1. Naive Solution :
## - iterate thru string with a nested loop
## - find all possible string strip & while saving the seen char in a set
## 2. Optimized & pointers :
## - save the letters in a dict, as key : index
## - I will have two pointers : start, end
## - if found duplicate , change key value to index & send start to index.

## I solved it, but i submitted too many times, failing in various test cases.. I should set my own test cases first....
## Edge cases : "pwwkew", "dvdf", "tmmzuxt", "aabaab!bb"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        seen = {}
        max_length = 0
        for i, char in enumerate(s):
            end += 1
            if char in seen:
                if start < seen[char] + 1:
                    start = seen[char] + 1
            if end - start > max_length:
                max_length = end-start
            seen[char] = i
        return max_length
            