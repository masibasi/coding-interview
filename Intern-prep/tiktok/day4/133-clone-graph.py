# https://leetcode.com/problems/clone-graph/
# 133-clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloneMap = {}

        def dfs(n):
            if n in cloneMap:
                return cloneMap[n]

            copy = Node(n.val)
            cloneMap[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)