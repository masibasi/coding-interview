# https://leetcode.com/problems/rotting-oranges/
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot_q = deque([])
        fresh = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rot_q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        ans = -1
        if fresh == 0:
            return 0

        while rot_q:
            for _ in range(len(rot_q)):
                r, c = rot_q.popleft()
                dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if grid[nr][nc] == 1:
                            rot_q.append((nr, nc))
                            grid[nr][nc] = 2
                            fresh -= 1
            ans += 1
        
        if fresh != 0:
            return -1
        return ans
