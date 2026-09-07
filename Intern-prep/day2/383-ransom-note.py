# Idea :
## 1. Brute force :
## - turn magazine into an array.
## - iterate thru ransomnote, check array (nested loop), check true -> false if used
## 2. Optimze using set
## - turn magazine into set, key : char, value : count
## - reduce count for every char in ransomnote.
## - return false if key is missing or value is already 0

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
# magazine_set = {}
# for char in magazine:
#     magazine_set[char] = magazine_set.get(char, 0) + 1
# for char in ransomNote:
#     if char in magazine_set:
#         if magazine_set[char] == 0:
#             return False
#         else:
#             magazine_set[char] -= 1
#     else:
#         return False
# return True

## Soulution from GPT : use Counter
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        return True
