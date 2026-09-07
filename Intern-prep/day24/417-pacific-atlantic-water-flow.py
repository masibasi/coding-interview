# https://leetcode.com/problems/pacific-atlantic-water-flow/
# 417-pacific-atlantic-water-flow


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # 범위 밖이면 스킵
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                # 이미 방문했거나, "역방향"으로 못 올라가는 경우 스킵
                if visited[nr][nc]:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr, nc, visited)

        # 태평양: 위쪽 행 + 왼쪽 열에서 시작
        for c in range(cols):
            dfs(0, c, pacific)  # top row
        for r in range(rows):
            dfs(r, 0, pacific)  # left col

        # 대서양: 아래쪽 행 + 오른쪽 열에서 시작
        for c in range(cols):
            dfs(rows - 1, c, atlantic)  # bottom row
        for r in range(rows):
            dfs(r, cols - 1, atlantic)  # right col

        ans = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    ans.append([r, c])

        return ans

        # rows = len(heights)
        # cols = len(heights[0])

        # check_flow = [[[0,0] for _ in range(cols)] for _ in range(rows)]

        # pacific_dirs = [(-1,0), (0,-1)]
        # atlantic_dirs = [(1,0), (0,1)]

        # def dfs(r,c, pac, atl):
        #     if pac == True:
        #         for dr, dc in pacific_dirs:
        #             if 0 > dr + r or 0 > dc + c:
        #                 check_flow[r][c][0] = 1
        #             elif heights[dr + r][dc + c] <= heights[r][c]:
        #                 dfs(dr+r,dc+c, True, False)
        #     if atl == True:
        #         for dr, dc in atlantic_dirs:
        #             if rows == dr + r or cols == dc + c:
        #                 check_flow[r][c][1] = 1
        #             elif heights[dr + r][dc + c] <= heights[r][c]:
        #                 dfs(dr+r,dc+c, False, True)

        # for i in range(rows):
        #     for j in range(cols):
        #         dfs(i,j, True, True)

        # ans = []
        # for i in range(rows):
        #     for j in range(cols):
        #         if check_flow[i][j] == [1,1]:
        #             ans.append([i,j])

        # return ans
