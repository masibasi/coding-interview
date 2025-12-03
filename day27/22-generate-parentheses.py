# https://leetcode.com/problems/generate-parentheses/
# 22-generate-parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(path, need_close, can_open):
            if len(path) == n * 2:
                ans.append(path)
                return
            if can_open > 0:
                dfs(path + "(", need_close + 1, can_open - 1)
            if need_close > 0:
                dfs(path + ")", need_close - 1, can_open)

        dfs("", 0, n)

        return ans
