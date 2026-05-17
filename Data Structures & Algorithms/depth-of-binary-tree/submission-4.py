# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs
# time O(N) space O(1)
#
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base 
        if not root:
            return 0

        #add one for current 
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))