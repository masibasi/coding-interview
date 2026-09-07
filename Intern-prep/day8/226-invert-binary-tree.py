# https://leetcode.com/problems/invert-binary-tree/
# 226-invert-binary-tree

# idea : bfs로 내려가면서 순차적으로 순서를 바꾸면 되지 않을까?
# - if reach child : return node
# - assign each opposite
# edge cases : 
# - root is null : return root
# - only left or right child? np



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        left, right = None, None
        if not root.left:
            left = self.invertTree(root.right)
            right = None
        elif not root.right:
            left = None
            right = self.invertTree(root.left)
        else:
            left = self.invertTree(root.right)
            right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root
