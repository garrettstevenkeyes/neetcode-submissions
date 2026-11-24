# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #space pointers
        slow, fast = head, head
        for i in range(n):
            fast = fast.next

        #iterate 
        while fast:
            slow = slow.next
            fast = fast.next

        if slow is head:
            return head.next

        #repoint
        res = curr = head
        while curr:
            if curr.next is slow:
                curr.next = curr.next.next
            
            curr = curr.next

        return res
