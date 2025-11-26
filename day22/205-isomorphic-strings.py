# https://leetcode.com/problems/isomorphic-strings/submissions/1839724914/
# 205-isomorphic-strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        worddict = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in worddict:
                if worddict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in worddict.values():
                    return False
                worddict[s[i]] = t[i]

        return True
