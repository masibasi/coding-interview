# https://leetcode.com/problems/number-of-provinces/
# 547-number-of-provinces


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n

        def dfs(node):
            if visited[node] == True:
                return
            visited[node] = True
            for to_node, connected in enumerate(isConnected[node]):
                if connected == 1 and to_node != node:
                    dfs(to_node)

        count = 0
        for i in range(n):
            if visited[i] == False:
                dfs(i)
                count += 1

        return count
