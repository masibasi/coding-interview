# https://leetcode.com/problems/max-area-of-island/
# 695-max-area-of-island


# Idea. :
# - 섬개수 찾듯이 일단 DFS 함수를 만들자
# - DFS 함수가 recursive하게 자기 숫자를 리턴하도록 해서 총 크기를 리턴하자
# - DFS 결과마다 비교해서 max 값 저장하자
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])

        def DFS(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
                return 0
            # 방문
            grid[r][c] = 0
            return 1 + DFS(r + 1, c) + DFS(r - 1, c) + DFS(r, c + 1) + DFS(r, c - 1)

        max_size = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_size = max(max_size, DFS(i, j))
        return max_size
