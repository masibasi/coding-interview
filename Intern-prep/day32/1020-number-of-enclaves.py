# https://leetcode.com/problems/number-of-enclaves/
# 1020-number-of-enclaves

# I think for the first & last rows and columns you can first search for land & turn them to 0 & don't count for land cells
# then for the inside just normally dfs and find the area of land.


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0  # visit
            land = 1
            for dr, dc in dirs:
                land += dfs(dr + r, dc + c)
            return land

        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    if grid[i][j] == 1:
                        dfs(i, j)

        count = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 1:
                    count += dfs(i, j)

        return count
