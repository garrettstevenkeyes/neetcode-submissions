# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#brainstorm
# head = [1,2,3,4], n = 2
#.            b    
#                 a
#         
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # If removing the head
        if n == length:
            return head.next

        # Otherwise, find the node before the one to remove
        curr = head
        for _ in range(length - n - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head