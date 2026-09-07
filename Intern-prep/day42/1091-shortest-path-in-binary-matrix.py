# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# 1091-shortest-path-in-binary-matrix

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # edge cases:
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if n == 1:
            return 1

        q = deque([(0,0)])
        visited = set()
        visited.add((0,0))

        length = 1

        while q:
            length += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (1, 1), (1,-1), (-1, 0), (-1, 1), (-1, -1)]:
                    nr, nc = r + dr, c + dc
                    if not 0 <= nr < n or not 0 <= nc < n:
                        continue
                    if (nr, nc) in visited:
                        continue
                    if nr == n-1 and nc == n-1:
                        return length
                    if grid[nr][nc] == 0:
                        q.append((nr,nc))
                        visited.add((nr,nc))
        return -1