# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        head = ListNode()
        dummy.next = head
        temp = 0

        while (l1 and l2):
            temp = temp + l1.val + l2.val
            new = ListNode(temp%10)
            temp = temp // 10
            head.next = new
            head = new

            l1, l2 = l1.next, l2.next
        
        while temp != 0 or l1 or l2:
            if l1:
                temp = temp + l1.val
                l1 = l1.next
            if l2:
                temp = temp + l2.val
                l2 = l2.next
            new = ListNode(temp%10)
            temp = temp // 10
            head.next = new
            head = new

        return dummy.next.next