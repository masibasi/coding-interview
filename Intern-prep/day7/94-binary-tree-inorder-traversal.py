# https://leetcode.com/problems/binary-tree-inorder-traversal/
# 94-binary-tree-inorder-traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )
        # if root.left:
        #     if not root.right:
        #         print([1, root.val])
        #         return self.inorderTraversal(root.left).append(root.val)
        #     else:
        #         print([2, root.val])
        #         left = self.inorderTraversal(root.left).append(root.val)
        #         print(left)
        #         return left.append(self.inorderTraversal(root.right))
        # if not root.left:
        #     if not root.right:
        #         print([3, root.val])
        #         return [].append(root.val)
        #     else:
        #         print([4, root.val])
        #         root_val = [].append(root.val)
        #         return root_val.append(self.inorderTraversal(root.right))
