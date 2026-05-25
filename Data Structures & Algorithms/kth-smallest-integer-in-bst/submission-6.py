# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None

        def dfs(node):
            nonlocal res
            nonlocal k

            #base case if not node or we have a result
            if not node or res != None:
                return

            #recurse left
            dfs(node.left)

            #do k -= 1
            k -= 1

            #if k equals 0
            if k == 0:
                #make the res equal to the node
                res = node.val
            
            #traverse right
            dfs(node.right)
        
        dfs(root)
        return res
