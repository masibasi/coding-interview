# https://leetcode.com/problems/rotting-oranges/
# 994-rotting-oranges

# BFS를 써야할거같음
# 한비퀴 쭉 돌고 로튼 있으면 큐에 삽입


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # 초기 상태: 썩은 오렌지(2)는 큐에, 신선한(1)은 개수 세기
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        mins= 0
        dirs = [(1,0), (-1, 0), (0,1), (0,-1)]
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            mins += 1

        return mins if fresh == 0 else -1
                        