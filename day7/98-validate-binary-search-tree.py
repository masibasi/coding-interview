# https://leetcode.com/problems/binary-tree-level-order-traversal/
# 102-binary-tree-level-order-traversal
# idea : BFS
# bfs로 돌리면서 각각을 어레이에 담고 리스트로 집어넣으면 되지 않을까?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            temp = []

            for _ in range(len(q)):
                nxt = q.popleft()
                temp.append(nxt.val)
                if nxt.left:
                    q.append(nxt.left)
                if nxt.right:
                    q.append(nxt.right)
            res.append(temp)
        return res
