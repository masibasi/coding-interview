# https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        nums.sort()

        def dfs(num_list, perm):
            if len(num_list) == 0:
                ans.add(tuple(perm))

            for i, num in enumerate(num_list):
                dfs(num_list[:i] + num_list[i+1:], perm + [num])


        dfs(nums, [])

        return list(ans)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False] * len(nums)
        ans = []
        def dfs(path):
            if len(path) == len(nums):
                ans.append(path[:])

            for i, num in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue

                if not visited[i]:
                    path.append(num)
                    visited[i] = True

                    dfs(path)

                    path.pop()
                    visited[i] = False

        dfs([])

        return ans