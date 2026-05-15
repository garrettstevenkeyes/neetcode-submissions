# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Brainstorm
# Time O(n)
# Space O(1)

# Plan
# 1. find middle of list
# 2. reverse list
# 3. merge the lists
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        default = ListNode(0, head)
        slow = head
        fast = head
        # 1. find middle of list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. reverse list
        cur = slow.next
        prev = None
        slow.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        # 3. merge the lists
        first = head
        second = prev

        while second:
            # Save the next nodes before we change pointers
            first_next = first.next
            second_next = second.next
            
            # Insert second node after first node
            first.next = second
            second.next = first_next
            
            # Move to the next pair of nodes to merge
            first = first_next
            second = second_next
