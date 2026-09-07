# https://leetcode.com/problems/flood-fill/submissions/1842115333/
# 733-flood-fill
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        og_color = image[sr][sc]
        if color == og_color:
            return image

        # dfs
        def dfs(r, c):
            image[r][c] = color
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == og_color:
                    dfs(nr, nc)

        dfs(sr, sc)

        return image

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        og_color = image[sr][sc]

        if color == og_color:
            return image
        q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()
            image[r][c] = color
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == og_color:
                    q.append((nr, nc))

        return image
