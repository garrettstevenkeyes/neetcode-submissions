# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #define dfs function because we need to pass more than root
        def dfs(root):
            # if not root return true and 0
            if not root:
                return [True, 0]
            #go left 
            left = dfs(root.left)
            #go right
            right = dfs(root.right)
            #if left is true and right is true and the difference between them 
            balanced = (left[0] and right[0] and abs(left[1]-right[1])<= 1)
                
            #is <= 1 its true
            return [balanced, 1 + max(left[1], right[1])]

        res = dfs(root)
        return res[0]
