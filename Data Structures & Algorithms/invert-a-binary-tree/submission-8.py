# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#time O(N)
#space O(N)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        #swap 
        root.left, root.right = root.right, root.left
        #process left subtree
        self.invertTree(root.left)
        #process right subtree
        self.invertTree(root.right)
        return root
