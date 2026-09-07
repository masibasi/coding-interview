# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        mapping = {}
        mapped = set()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapped:
                    return False
                mapping[s[i]] = t[i]
                mapped.add(t[i])
        return True