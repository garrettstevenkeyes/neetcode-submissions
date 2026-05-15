# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        res = ListNode(0)
        finalVal = res
        while stack:
            newNode = ListNode(stack.pop())
            finalVal.next = newNode
            finalVal = finalVal.next
        
        return res.next
