# https://leetcode.com/problems/valid-sudoku/description/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for r in range(9):
            nums = defaultdict(int)
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                nums[num] += 1
                if nums[num] > 1:
                    return False
                    
        # col
        for c in range(9):
            nums = defaultdict(int)
            for r in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                nums[num] += 1
                if nums[num] > 1:
                    return False

        # square
        for i in range(3):
            for j in range(3):
                nums = defaultdict(int)
                for r in range(3):
                    for c in range(3):
                        num = board[r + 3*i][c + 3*j]
                        if num == '.':
                            continue
                        nums[num] += 1
                        if nums[num] > 1:
                            return False
        return True