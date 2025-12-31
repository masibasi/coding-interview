# https://leetcode.com/problems/redundant-connection/
# 684-redundant-connection

from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        # for node1, node2 in edges:
        #     graph[node1].append(node2)
        #     graph[node2].append(node1)

        n = len(graph)
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pa] > rank[pb]:
                parent[pb] = pa
            elif rank[pa] == rank[pb]:
                parent[pa] = pb
                rank[pb] += 1
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
