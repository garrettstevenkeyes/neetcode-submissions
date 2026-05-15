# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #define helper
        def helper(node, low, high):
            #if the node doesnt exist its true
            if not node: return True
            #if the node is not greater than the low and less than the high
            #its false
            if not (low < node.val < high):
                return False
            #return going left and right
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        #negative inf going left and positive inf going right
        return helper(root, float('-inf'), float('inf')) 