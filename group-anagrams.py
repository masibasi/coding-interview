# https://leetcode.com/problems/group-anagrams/
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[tuple(sorted(word))].append(word)
        ans = []
        for key, value in anagrams.items():
            ans.append(value)
        return ans