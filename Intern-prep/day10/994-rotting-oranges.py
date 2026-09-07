# https://leetcode.com/problems/rotting-oranges/
# 994-rotting-oranges

# Idea :
# - 동시에 4방향으로 썩으니까 BFS로 찾아야할거같다.
# - 일단 1이 존재안하면 리턴 0
# - 2가 없으면 리턴 -1
# - 2가 여러개 있을 수도 있겠는데??
# - 2가 있는 곳에서 동시에 BFS를 시행해야하는거같다.
# - 순회하면서 2가 있는 좌표를 큐에 먼저 집어넣고 이후에 각각 BFS를 진행하면 어떤가??
# - 총 몇 번 돌았는지 세어야하니까 리커시브하게 만들어야할거같은데맞나?


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        if len(q) == 0:
            return -1

        minutes = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:  # 이 조건이 중요하네
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1
