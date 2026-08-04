# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None

        #do dfs
        def dfs(node):
            nonlocal res
            nonlocal k

            #if not root or k == 0
            if not node or res != None:
                return 
            
            #go all the way left
            dfs(node.left)

            k -= 1

            if k == 0:
                res = node.val

            #if there is a right go right
            dfs(node.right)
        dfs(root)
        return res