# https://leetcode.com/problems/max-area-of-island/
# 695-max-area-of-island


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            visited[r][c] = 1
            area = 1
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and visited[nr][nc] != 1
                    and grid[nr][nc] == 1
                ):
                    area += dfs(nr, nc)
            return area

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] != 1 and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
