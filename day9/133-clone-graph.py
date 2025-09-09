# https://leetcode.com/problems/clone-graph/
# 133-clone-graph

# 이거는 그냥 순회하면서 새로 만들면 되는거같은데??
# self에다가 변수 만들어서하면 되지 않을까
# 리턴값은 뭐지 노드인가
# 이번엔 BFS로 해보자

## 어려웠다...


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        clones = {}  # {원래 노드: 새 노드}
        q = deque([node])
        clones[node] = Node(node.val)

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                nei_clone = Node(nei.val)
                if nei not in clones:
                    clones[nei] = nei_clone
                    q.append(nei)
                clones[cur].neighbors.append(clones[nei])

        return clones[node]
