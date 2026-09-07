# https://leetcode.com/problems/flood-fill/description/
# 733-flood-fill


# Edge case 생각하기!!
# - 시작색과 채울색이 같은경우!!
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        self.start_col = image[sr][sc]
        self.color = color
        if self.start_col == color:
            return image

        def dfs(r, c):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or image[r][c] != self.start_col
            ):
                return
            image[r][c] = self.color
            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r - 1, c)

        dfs(sr, sc)
        return image
