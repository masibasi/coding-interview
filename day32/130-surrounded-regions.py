# https://leetcode.com/problems/surrounded-regions/
# 130-surrounded-regions


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols:
                return True  # found edge
            if board[r][c] == "X":  # not Region
                return False
            if board[r][c] == "V":  # Visited
                return False

            found_edge = False
            board[r][c] = "V"  # Visit

            for dr, dc in dirs:
                found_edge = found_edge or dfs(dr + r, dc + c)
            if found_edge == True:
                return True

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if board[i][j] == "O":
                    found_edge = dfs(i, j)
                    if found_edge:
                        for r in range(rows):
                            for c in range(cols):
                                if board[r][c] == "V":
                                    board[r][c] = "O"
                    else:
                        for r in range(rows):
                            for c in range(cols):
                                if board[r][c] == "V":
                                    board[r][c] = "X"
