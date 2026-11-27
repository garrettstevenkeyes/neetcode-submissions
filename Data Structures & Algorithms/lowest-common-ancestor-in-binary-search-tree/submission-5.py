# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #if they are split then return the current 
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root

        #if they are to the left recurse
        elif (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)

        #if they are to the right recurse
        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return root