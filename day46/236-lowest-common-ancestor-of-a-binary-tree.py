# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 그냥 DFS로 내려가면서 찾으면 찾은거리턴 튜플로 하면 어떨까?
        # 둘다 해결 된 순간 리턴


        def dfs(node:TreeNode) -> int: 
            if not node:
                return 0
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            return left if left else right

        return dfs(root)