# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Brainstorm
# Time(N)
# Space O(1)

#1. define a next and prev place holder

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev