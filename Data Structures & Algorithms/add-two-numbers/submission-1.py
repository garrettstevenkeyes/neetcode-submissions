# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 321.  [1,2,3]
# 765.  [5,6,7]
# carry = 0
#
# 321.  [7,8,9]
# 765.  [5,6,7]
#            i
#       [2,5,1,7]
# carry = 1
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create dummy list and set cur
        dummy = ListNode()
        cur = dummy
        #define carry 
        carry = 0
        #if we have num1, num2, or a carry
        while l1 or l2 or carry:
            #get values from nodes
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            #calculate new value
            #get tens place for carry 
            #get ones place for add
            #create node
            val = v1+v2+carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            #iterate
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

