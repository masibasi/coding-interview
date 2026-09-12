# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = deque([])

        dummy = ListNode()
        dummy.next = head
        temp = dummy

        while head:
            queue.append(head)
            head = head.next

        for i in range(len(queue)):
            if i % 2 == 0:
                temp.next = queue.popleft()
            else:
                temp.next = queue.pop()
            temp = temp.next

        temp.next = None

        return dummy.next

    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first, second = head, prev
        
        dummy = ListNode()
        dummy.next = head
        while second.next:  # second가 마지막 노드(뒤집힌 절반의 원래 첫 노드)에 도달하면 멈춤
            tmp1, tmp2 = first.next, second.next  # 다음으로 이동할 노드들을 먼저 저장
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return dummy.next
