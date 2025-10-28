class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        q = deque([(0, 0, 1)])  # (row, col, distance)
        visited = set([(0, 0)])  # 방문한 셀 추적

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        while q:
            r, c, dist = q.popleft()

            # 도착지에 도달하면 거리 반환
            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # grid 안에 있고, 통로(0)이며, 아직 방문하지 않은 경우
                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and grid[nr][nc] == 0
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))

        return -1
