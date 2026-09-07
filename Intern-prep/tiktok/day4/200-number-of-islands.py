# https://leetcode.com/problems/number-of-islands/
# 200-number-of-islands

# DFS로 한 번 돌고 1을 0으로 다 지워버려야할거같다
# BFS로도 한 번 해봐야겠다

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if not grid:
            return 0
        # def dfs(r, c):
        #     if r < 0 or r >= rows or c < 0 or c >= cols:
        #         return
        #     if grid[r][c] == "0":
        #         return
        #     grid[r][c] = "0"    
        #     dfs(r+1, c)
        #     dfs(r-1, c)
        #     dfs(r, c+1)
        #     dfs(r, c-1)

        # count = 0
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == "1":
        #             count += 1
        #             dfs(row, col)

        def bfs(sr: int, sc: int) -> None:
            q = deque([(sr, sc)])
            grid[sr][sc] = "0"            # 방문 표시(침수)
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr,nc))

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        return count