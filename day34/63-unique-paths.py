# https://leetcode.com/problems/unique-paths-ii/description/
# 63-unique-paths

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # idea : DP
        # DP[i,j] => numer of unique paths from 0,0 to i,j
        # DP[i,j] = DP[i-1][j] + DP[i][j-1]
        if obstacleGrid[0][0] == 1:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        DP = [[0 for _ in range(cols)] for _ in range(rows)]
        DP[0][0] = 1

        for i in range(1, rows):
            if obstacleGrid[i][0] != 1 and DP[i-1][0] == 1:
                DP[i][0] = 1
        for i in range(1, cols):
            if obstacleGrid[0][i] != 1 and DP[0][i-1] == 1:
                DP[0][i] = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] != 1:
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]

        return DP[rows-1][cols-1]