# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]

        board = [["."] * n for _ in range(n)]
        ans = []

        cols = set()      # 열
        diag1 = set()     # 우하향 대각선 (r - c)
        diag2 = set()     # 우상향 대각선 (r + c)

        def dfs(row):
            # Base Case: 마지막 행까지 무사히 퀸을 다 채웠다면 성공!
            if row == n:
                # 현재 보드 상태를 문자열 리스트로 변환해서 저장
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                board[row][col] = "Q"
                dfs(row+1)

                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
                board[row][col] = "."

        dfs(0)

        return ans