# https://leetcode.com/problems/subsets/
# 78-subsets

# idea :
## window size change -> slide?
## 부분집합 원소 개수로 어떻게 뽑아내야 하려나?


## 넣을지 말지를 각 원소마다 판단하면 되겠다!
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(start, path):
            ans.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return ans
