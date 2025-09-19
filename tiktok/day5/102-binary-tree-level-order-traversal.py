class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        start_color = image[sr][sc]
        if start_color == color:
            return image
            
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            if image[r][c] != start_color:
                return
            image[r][c] = color

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image