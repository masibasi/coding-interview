# https://leetcode.com/problems/number-of-provinces/
# 547-number-of-provinces
# 그래프로 표현하면 될거같은데?
# 그러고 나서 q로 dfs 돌리면 될거같고
# 방문 그리드를 유지하면 좋을거같음.


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        graph = {i: [] for i in range(size)}
        for i in range(size):
            for j in range(size):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)

        visited = [0] * size
        count = 0

        def dfs(i):
            if visited[i] == 1:
                return
            visited[i] = 1
            for nxt in graph[i]:
                dfs(nxt)

        for i in range(size):
            if visited[i] == 0:
                dfs(i)
                count += 1

        return count
