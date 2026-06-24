# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #we are just comparing tree nodes, so we can use this function to do it
        #base case they dont exist
        if not p and not q: return True
        #if p and not q, or if not p and q its false
        if (p and not q) or (not p and q): return False
        #if both are there but they are not equal its false
        if p.val != q.val: return False
        #iterate
        return self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)
        
