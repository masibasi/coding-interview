# https://leetcode.com/problems/invert-binary-tree/
# 226-invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        q = deque([root])

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                left, right = cur.right, cur.left
                cur.left, cur.right = left, right
                if left:
                    q.append(left)
                if right:
                    q.append(right)
        return root