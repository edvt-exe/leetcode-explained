# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        node1 = temp
        node2 = temp

        for i in range(n + 1):
            node2 = node2.next

        while node2:
            node1 = node1.next
            node2 = node2.next

        node1.next = node1.next.next
        return temp.next