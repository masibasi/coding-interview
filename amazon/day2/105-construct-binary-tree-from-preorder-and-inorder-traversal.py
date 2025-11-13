# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def buildTree(preorder, inorder):
            if not preorder or not inorder:
                return None
            root_val = preorder[0]
            mid = inorder.index(root_val)
            root = TreeNode(root_val)

            root.left = buildTree(preorder[1 : mid + 1], inorder[:mid])
            root.right = buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
            return root

        return buildTree(preorder, inorder)
