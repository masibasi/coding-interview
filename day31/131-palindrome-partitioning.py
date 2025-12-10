# https://leetcode.com/problems/palindrome-partitioning/
# 131-palindrome-partitioning


# GOt help from GPT
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def is_pal(string):
            l, r = 0, len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []

        def dfs(start, path):
            if start == n:
                res.append(path[:])
                return
            for i in range(start, n):
                if is_pal(s[start : i + 1]):
                    dfs(i + 1, path + [s[start : i + 1]])

        dfs(0, [])

        return res

    # def partition(self, s: str) -> List[List[str]]:
