# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        dummy = ListNode()
        dummy.next = head
        lists = [dummy]
        while head:
            lists.append(head)
            head = head.next
        length = len(lists)
        prev = lists[length-n-1]
        prev.next = prev.next.next
        return dummy.next

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode()

        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next