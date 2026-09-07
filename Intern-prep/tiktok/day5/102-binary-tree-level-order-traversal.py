# https://leetcode.com/problems/binary-tree-level-order-traversal/
# 102-binary-tree-level-order-traversal


# 아이디어

# 그냥 BFS 하면 될거같은데??


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])

        ans = []
        while q:
            temp = []
            for _ in range(len(q)):
                cur = q.popleft()
                temp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(temp)
        return ans
