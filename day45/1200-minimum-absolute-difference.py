# https://leetcode.com/problems/minimum-absolute-difference/?envType=daily-question&envId=2026-01-26

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        prev = arr[0]
        min_diff = abs(arr[0] - arr[1])
        for i in range(1,len(arr)):
            diff = abs(prev - arr[i])
            if diff < min_diff:
                min_diff = diff
            prev = arr[i]

        prev = arr[0]
        ans = []
        for i in range(1,len(arr)):
            diff = abs(prev - arr[i])
            if diff == min_diff:
                ans.append([prev, arr[i]])
            prev = arr[i]

        return ans