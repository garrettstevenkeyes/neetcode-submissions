# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #if not root return none
        if not root: return
        #set left to the right
        root.left, root.right = root.right, root.left
        #set the right to the left
        #recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root