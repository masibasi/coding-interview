# https://leetcode.com/problems/permutation-in-string
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        count = Counter(s1)
        cand = Counter(s2[:n])

        if count == cand:
            return True

        for i in range(n, len(s2), 1):    
            cand[s2[i]] += 1
            if cand[s2[i-n]] == 1:
                del cand[s2[i-n]]
            else:
                cand[s2[i-n]] -= 1

            if count == cand:
                return True

        return False