# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# 235-lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Idea :
# - 직관적으로 DFS로 풀어야할 것 같다 (수직으로 내려가면서 조상을 찾아야할거같음)
# - p != q임.
# 모든 값이 unique임.
# - 한 값을 찾을때까지 지나온 ancesters의 어레이를 가록해야할거같은 느낌.
# - stack으로 지나가는 node들을 기록해놓고 다 검색한 노드는 pop 해버리면 어떨까?
# - 두 값을 모두 찾은 순간 stack 최상단에 있는 값이 LCA임.
# - 가능할 것 같다 ! 해보자

# - 아 바보 이거 이진검색트리구나 그러면 각각 거기 있는 이유가 있어.
# - p랑 q가 각각 검색하는 노드보다 큰지 작은지 확인하면서 가면 좋을거같아
# (GPT)

# 핵심 아이디어 (BST 성질)
# 	•	p.val과 q.val이 모두 현재 노드 값보다 작다 → LCA는 왼쪽 서브트리에 있음 → root = root.left
# 	•	둘 다 크다 → LCA는 오른쪽 서브트리에 → root = root.right
# 	•	위 두 경우가 아니면(한쪽은 작고 한쪽은 크거나, 현재 노드가 p/q 중 하나) 현재 노드가 LCA
# 이런 성질을 사용했어야했다...


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return root
        cur = root
        pv, qv = p.val, q.val
        while cur:
            if pv < cur.val and qv < cur.val:
                cur = cur.left
            elif cur.val < pv and cur.val < qv:
                cur = cur.right
            else:
                return cur
