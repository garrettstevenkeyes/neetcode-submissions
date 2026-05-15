# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Brainstorm 
# define helper for repeatedly checking if tree if valid
# you check all the children trees to verify

#Plan
#we check the node, low, and high
#1. if not node its true
#2. if low if not < node < high, its false
#3. recurse
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            #1. if not node its true
            if not node: return True
            #2. if low if not < node < high, its false
            if not (low < node.val < high): return False
            #3. recurse
            return helper(node.left, low,node.val) and helper(node.right, node.val, high)
        return helper(root, float('-inf'), float('inf'))