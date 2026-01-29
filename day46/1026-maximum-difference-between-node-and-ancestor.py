# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/submissions/1901449807/
# 1026-maximum-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # DFS로 high, low 갖고 다니면서 돌아다니면 될듯?


        def dfs(node, high, low):
            if not node:
                return high - low
            high = max(high, node.val)
            low = min(low, node.val)

            left_diff = dfs(node.left, high, low)
            right_diff = dfs(node.right, high, low)

            return max(left_diff, right_diff)

    
        return dfs(root, root.val, root.val)