# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time O(N)
# Space O(N)

#1. if not one list return the other
#2. while both exist if one node <= to the other add, otherwise add the other
#3. while list1 add to res
#4 while list2 add to result

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        finalRes = res
        #1. if not one list return the other
        if not list1: return list2
        if not list2: return list1
        #2. while both exist if one node <= to the other add, otherwise add the other
        while list1 and list2:
            if list1.val <= list2.val:
                res.next = ListNode(list1.val)
                list1 = list1.next
            else:
                res.next = ListNode(list2.val)
                list2 = list2.next
            res = res.next
        #3. while list1 add to res
        while list1:
            res.next = ListNode(list1.val)
            res = res.next
            list1 = list1.next
        #4 while list2 add to result
        while list2:
            res.next = ListNode(list2.val)
            res = res.next
            list2 = list2.next
        
        return finalRes.next