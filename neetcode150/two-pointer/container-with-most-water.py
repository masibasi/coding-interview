# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            h = min(height[l], height[r])
            v = h * (r - l)
            ans = max(ans, v)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans