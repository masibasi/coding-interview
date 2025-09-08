# https://leetcode.com/problems/validate-binary-search-tree/
# 98-validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Idea :
# 1. DFS로 내려갈때 left 가 return하는거는 자기보다 무조건 작아야하는 조건, right는 자기보다 큰 조건을 걸면 되지 않을까?
# - root가 없을때 조건 만들기
# - left, right가 없을 때 조건 만들기
# - 근데 이렇게 하면 마지막에 어떻게 True를 반환하지?
# - 함수로 만들어서 숫자가 반환되면 True로 바꿔줘야하나


# - Idea: DFS with (low, high) range; or inorder strictly increasing
# - Why it works: BST property must hold for **all descendants**, so pass constraints down
# - Big-O: O(n) time, O(h) space
# - Edge cases: empty tree, single node, skewed tree, duplicates (must be False)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high) -> bool:
            if not node:
                return True
            # 현재 노드는 (low, high) 범위 안에 있어야 함
            if not (low < node.val < high):
                return False
            # 왼쪽은 high를 현재 값으로, 오른쪽은 low를 현재 값으로 업데이트
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))
