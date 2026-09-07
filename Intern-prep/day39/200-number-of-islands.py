# https://leetcode.com/problems/number-of-islands/
# 200-number-of-islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        ans = 0

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols:
                return
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dfs(r + dr, c + dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1

        return ans
