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
        if not head or not head.next:
            return

        p1 = head
        p2 = head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        second = p1.next
        prev = None
        p1.next = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2