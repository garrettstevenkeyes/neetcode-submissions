# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res= None

        def dfs(node):
            nonlocal res
            nonlocal k
            #if there is no node return as base case
            if not node:
                return
            #go left to bottom value
            dfs(node.left)
            #subtract from the count k
            k -= 1
            #if k equals 0 we have hit our target
            #set the result value
            if k == 0:
                res = node.val
            #go right if its possible
            dfs(node.right)

        #call the function
        dfs(root)
        #return the result
        return res

