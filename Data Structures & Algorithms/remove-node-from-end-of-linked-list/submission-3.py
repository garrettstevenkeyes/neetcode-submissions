# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Brainstorm
# Time O(N)
# Space O(1)

#Plan
#1. create two pointers, one one less than the other
#2. while the first exists iterate it
#3. iterate the second
#4. make the second skip and point to the next.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        #create gap
        for _ in range(n):
            fast = fast.next
        
        #get to list end
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

