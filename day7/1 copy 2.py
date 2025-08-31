# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 104-maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. DFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)
#         return 1 + max(left, right)


# 2. BFS
# from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            for _ in range(len(q)):
                nxt = q.popleft()
                if nxt.left:
                    q.append(nxt.left)
                if nxt.right:
                    q.append(nxt.right)
            depth += 1
        return depth
