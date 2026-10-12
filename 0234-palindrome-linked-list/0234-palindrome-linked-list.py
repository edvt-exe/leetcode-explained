# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        def reverse_list(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev

        cop = ListNode(0)
        tail = cop
        curr = head

        while curr:
            tail.next = ListNode(curr.val)
            tail = tail.next
            curr = curr.next
        
        curr1 = head
        curr2 = reverse_list(cop.next)

        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False

            curr1 = curr1.next
            curr2 = curr2.next

        return True