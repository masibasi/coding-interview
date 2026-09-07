# https://leetcode.com/problems/binary-tree-right-side-view/
# 199-binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# I think I can approach this as bfs.
# while traversing every level, I can store the last node found
# in the level.


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        ans = []
        while q:
            cur = None
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(cur.val)

        return ans
