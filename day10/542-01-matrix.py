# https://leetcode.com/problems/01-matrix/
# 542-01-matrix

# idea
# - 이거도 각각 돌면서 1이 있는 곳에서 BFS를 하고 값을 리턴하면 될거같다.
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        dist = [[-1] * cols for _ in range(rows)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if 0 <= nx < rows and 0 <= ny < cols and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        return dist


# 2pass dp로도 풀 수 있음

# from typing import List

# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         m, n = len(mat), len(mat[0])
#         INF = 10**9
#         dist = [[0 if mat[i][j] == 0 else INF for j in range(n)] for i in range(m)]

#         # 1) top-left -> bottom-right
#         for i in range(m):
#             for j in range(n):
#                 if dist[i][j] != 0:
#                     if i > 0:
#                         dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
#                     if j > 0:
#                         dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)

#         # 2) bottom-right -> top-left
#         for i in range(m-1, -1, -1):
#             for j in range(n-1, -1, -1):
#                 if dist[i][j] != 0:
#                     if i < m-1:
#                         dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
#                     if j < n-1:
#                         dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)

#         return dist
