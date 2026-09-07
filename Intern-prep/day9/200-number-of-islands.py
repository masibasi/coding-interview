# https://leetcode.com/problems/number-of-islands/
# 200-number-of-islands
# Idea :
# - 뭔가 recursive 하게 1인 값을 찾아떠날 수 있지 않을까
# - 중요한건 방문한 곳들은 방문했다고 적어야할거같다.


class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     visited = set()
    #     islands = 0
    #     def dfs(r,c):
    #         if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" or (r, c) in visited:
    #             return
    #         visited.add((r,c))
    #         dfs(r+1, c)
    #         dfs(r, c+1)
    #         dfs(r-1, c)
    #         dfs(r, c-1)

    #     rows, cols = len(grid), len(grid[0])
    #     for row in range(rows):
    #         for col in range(cols):
    #             if (row, col) not in visited and grid[row][col] == "1":
    #                 islands += 1
    #                 dfs(row,col)
    #     return islands
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # 범위 벗어나거나 바다(0)이면 stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"  # 방문 처리
            # 상하좌우 탐색
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands
