/**
 * Definition for singly-linked list.
 * class ListNode {
 *     var val: Int
 *     var next: ListNode?
 *     init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        if list1 == nil {
            return list2
        }
        if list2 == nil {
            return list1
        }

        var l1 = list1
        var l2 = list2

        var res: ListNode? = ListNode(0)
        let returnedRes = res

        while l1 != nil && l2 != nil {
            if l1!.val <= l2!.val {
                res!.next = ListNode(l1!.val)
                l1 = l1!.next
            } else {
                res!.next = ListNode(l2!.val)
                l2 = l2!.next
            }
            res = res!.next
        }

        while l1 != nil {
            res!.next = ListNode(l1!.val)
            l1 = l1!.next
            res = res!.next
        }

        while l2 != nil {
            res!.next = ListNode(l2!.val)
            l2 = l2!.next
            res = res!.next
        }

        return returnedRes!.next
    }
}
