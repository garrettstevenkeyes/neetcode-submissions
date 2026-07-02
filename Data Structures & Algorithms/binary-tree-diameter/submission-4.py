# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # init res
        res = 0
        
        #define dfs, input is node
        def dfs(node):
            #make the res not local
            nonlocal res

            #if not root base case of 0
            if not node: return 0
            #iterate left
            left = dfs(node.left)
            #iterate right
            right = dfs(node.right)

            res = max(res, left + right)

            return 1 + max(left, right)
        
        #call dfs
        dfs(root)
        #return res
        return res