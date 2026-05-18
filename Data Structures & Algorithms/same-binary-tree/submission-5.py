# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#time. O(N)
#space O(1)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if node doesnt exist return true
        if not p and not q:
            return True
        #compare tree children
        if (p and not q) or (not p and q):
            return False
        #compare node values
        if p.val != q.val:
            return False
        # call function
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)