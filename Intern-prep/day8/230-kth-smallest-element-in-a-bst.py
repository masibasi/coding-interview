# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# 230-kth-smallest-element-in-a-bst

# Idea
# - DFS로 제일 내려거서 1부터 카운팅하면 되지 않을까?
# - 일단 뭐가 되었든 내 노드 기준으로 왼오른이 작고 큰거니까 recursive 하게 풀어야할거같다.
# - recursive인건 보통 DFS이니까 생각해볼까?
# - 아 아니다 이거는 스택을 사용한 dfs로 가야할거같다.
# - 일단은 left = 내 순서 - 1이고 right는 내 순서 + 1이다.
# - 내 순서를 아는건 가장 작은 값이 유일하다.
# - 거꾸로 생각하면 내 순서는 left순서 + 1이고 right 순서 - 1이다.
# - 가장 작은값은 right 쪽에서 나올 수 없다.
# - 왼쪽에서만 나올 수 있다.

# - #### 알고보니 BST라서 inorder로 돌리면 오름차순으로 나옴
# - #### 그래서 k번째로 pop하는게 답이 된다.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        count = 0

        # 왼쪽 끝까지 내려가기 → 하나씩 pop하며 방문(오름차순)
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left  # 왼쪽 최하단으로 이동 (제일 작은값)
            cur = stack.pop()
            count += 1
            if count == k:
                return cur.val
            cur = cur.right
