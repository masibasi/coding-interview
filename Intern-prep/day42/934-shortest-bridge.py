# https://leetcode.com/problems/shortest-bridge/
# 934-shortest-bridge

# what if I change 1 island to '2' to indicate different islands?
# start from all '2's -> '0' -> find '1'

# double loop do indicate an island.
# run dfs once to change all 1 to 2

# double loop to find 2
# run bfs for all 2.
#   if next is 2, return
#   if next is 0: continue
#   if next is 1: return path length
#   calculate the minimum path.

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs_indicate_island(r,c):
            if not 0 <= r < n or not 0 <= c < n:
                return
            if grid[r][c] == 0:
                return
            if grid[r][c] == 2:
                return
            grid[r][c] = 2

            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = r + dr, c + dc
                dfs_indicate_island(nr,nc)
        
        q = deque([])
        visited = set()

        complete = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not complete:
                    dfs_indicate_island(i,j)
                    complete = True
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))

        bridges = -1


        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if grid[x][y] == 1:
                    return bridges

                visited.add((x,y))

                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in visited and 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 2:
                        q.append((nx,ny))
                        visited.add((nx,ny))
            bridges += 1