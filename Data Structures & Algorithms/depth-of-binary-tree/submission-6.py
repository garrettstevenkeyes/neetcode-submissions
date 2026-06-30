# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case
        if not root:
            return 0
        
        #otherwise add one and recurse
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))