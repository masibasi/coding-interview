# https://leetcode.com/problems/balanced-binary-tree/
# 110-balanced-binary-tree

# idea :
# dfs으로 내려가면서, 나의 왼쪽의 depth와 오른쪽의 depth가 2이상 차이나면 false return 하면 되지 않을까
# 탐색하며 height를 찾다가 최대 깊이와 최저깊이를 계속 갖고있으면 되지 않을까?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True

#         def maxDepth(node):
#             if not node:
#                 return 0
#             left = maxDepth(node.left)
#             right = maxDepth(node.right)
#             return 1 + max(left, right)

#         def minDepth(node):
#             if not node:
#                 return 0
#             left = minDepth(node.left)
#             right = minDepth(node.right)
#             return 1 + min(left, right)

#         return abs(maxDepth(root) - minDepth(root)) < 2
# 틀림 -> 한쪽 subtree가 너무 작으면 반영 안됨...


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = height(node.left)
            if lh == -1:
                return -1
            rh = height(node.right)
            if rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)

        return height(root) != -1
