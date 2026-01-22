# https://leetcode.com/problems/regions-cut-by-slashes/
# 이문제는 뭔가 n * n을 3n * 3n으로 보고 매트릭스로 만들어서 사이클을 탐지하는 문제로 바꿔 풀 수 있을거같은데 맞아 ? 그냥 방향성만 잡아보려고
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)

        matrix = [[0 for _ in range(3*n)] for _ in range(3*n)]

        for i, row in enumerate(grid):
            prev = ''
            for j, char in enumerate(row):
                if char == ' ':
                    pass
                elif char == '/':
                    matrix[i * 3][j * 3 + 2] = 1
                    matrix[i * 3 + 1][j * 3 + 1] = 1
                    matrix[i * 3 + 2][j * 3] = 1
                elif char == '\\':
                    matrix[i * 3][j * 3] = 1
                    matrix[i * 3 + 1][j * 3 + 1] = 1
                    matrix[i * 3 + 2][j * 3 + 2] = 1

        # for row in matrix:
            # print(row)

        def dfs(r, c):
            if not 0 <= r < 3*n or not 0 <= c < 3*n:
                return
            if matrix[r][c] == 1:
                return
            matrix[r][c] = 1

            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        ans = 0
        for i in range(3 * n):
            for j in range(3 * n):
                if matrix[i][j] == 0:
                    dfs(i,j)
                    ans += 1

        return ans