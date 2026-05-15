# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if both dont exist true
        if not p and not q:
            return True
        #if one or the other doesnt exist false 
        if (p and not q) or (not p and q) or (p.val != q.val):
            return False
        #recurse
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)