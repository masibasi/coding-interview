# https://leetcode.com/problems/rotting-oranges/
# 994-rotting-oranges
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        q = deque([])
        # put rotten oranges in queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # already no fresh
        if fresh == 0:
            return 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            minutes += 1

        # not possible
        if fresh != 0:
            return -1

        return minutes - 1
