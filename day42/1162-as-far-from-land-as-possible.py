# https://leetcode.com/problems/as-far-from-land-as-possible/
# 1162-as-far-from-land-as-possible
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # edge cases:
        if n == 1:
            return -1

        q = deque([])

        check_0 = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))
                if grid[i][j] == 0:
                    check_0 = True

        if len(q) == 0:
            return -1
        if not check_0:
            return -1

        distance = -1

        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        while q:
            # print(len(q))
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if not 0 <= nr < n or not 0 <= nc < n:
                        continue
                    if grid[nr][nc] == 1:
                        continue
                    grid[nr][nc] = 1
                    q.append((nr,nc))
            distance += 1

        return distance