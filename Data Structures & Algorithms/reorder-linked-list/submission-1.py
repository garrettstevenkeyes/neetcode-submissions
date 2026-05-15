# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time O(N)
# Space O(1)

#Plan
#1. find middle of list
#2. reverse second half of list
#3. join lists
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        res = default = ListNode(0, head)
        slow = head
        fast = head

        #find midway point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse second half
        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        #join lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2