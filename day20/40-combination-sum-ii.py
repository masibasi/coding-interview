# https://leetcode.com/problems/combination-sum-ii/
# 40-combination-sum-ii


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, path, total):
            if total == target:
                res.append(path[:])

            if total > target:
                return

            for i in range(start, len(candidates)):
                if start < i and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, path + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return res
