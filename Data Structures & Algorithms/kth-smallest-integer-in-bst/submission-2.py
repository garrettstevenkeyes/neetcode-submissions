# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#brainstorm
# Time O(N)
# Space O(N)

#Plan
# BST so we know to the left is the least
# Save items in stack as we go
# when we run out of cur nodes, pop from stack 
# add 1
# traverse right and continues
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        n = 0
        stack = []
        # BST so we know to the left is the least
        while cur or stack:
            # Save items in stack as we go
            while cur:
                stack.append(cur)
                cur = cur.left

            # when we run out of cur nodes, pop from stack 
            cur = stack.pop()
            # add 1
            n += 1

            #if n == k return 
            if n == k:
                return cur.val
        
            # traverse right and continues
            cur = cur.right