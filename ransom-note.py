# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = defaultdict(int)

        for char in magazine:
            mag_letters[char] += 1

        for char in ransomNote:
            mag_letters[char] -= 1
            if mag_letters[char] < 0:
                return False

        return True