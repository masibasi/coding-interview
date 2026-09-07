# https://leetcode.com/problems/linked-list-cycle/submissions/1750688888/
# 141-linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. Brute Force
# = check thru [0, 10^4] count of all nodes, until you find self.next = null

# 2. create another Obj with prop : back. if it already has back, return true (not working)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         check = {}
#         back = None
#         while head:
#             if not head.next:
#                 return False
#             if check[head]['back']:
#                 return True
#             check[head] = {'back' : head}
#             back = head
#             head = head.next


# 3. just use set()
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            if not head.next:
                return False
            seen.add(head)
            head = head.next


# 4. Floyd
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False
