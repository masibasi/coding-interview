# https://leetcode.com/problems/combination-sum/?envType=problem-list-v2&envId=plakya4j
# 39-combination-sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()

        def helper(tar, used_nums):
            for cand in candidates:
                if tar - cand == 0:
                    combo = used_nums + [cand]
                    combo.sort()
                    ans.add(tuple(combo))
                elif tar - cand > 0:
                    helper(tar - cand, used_nums + [cand])

        helper(target, [])

        return [list(x) for x in ans]


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, path, total):
            if total == target:
                res.append(path[:])
                return
            elif total > target:
                return
            else:
                for i in range(start, len(candidates)):
                    path.append(candidates[i])
                    dfs(i, path, total + candidates[i])
                    path.pop()

        dfs(0, [], 0)
        return res

    def combinationSum(self, candidates, target):
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]  # sum = 0일 때는 빈 조합 하나

        for c in candidates:
            for k in range(c, target + 1):
                for comb in dp[k - c]:
                    dp[k].append(comb + [c])

        return dp[target]
