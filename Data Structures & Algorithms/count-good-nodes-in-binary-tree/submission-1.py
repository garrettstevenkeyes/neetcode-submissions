# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, maxSoFar):
            nonlocal res
            #eventually it always hits last node and returns
            if not root: 
                return

            if root.val >= maxSoFar:
                res += 1

            maxSoFar = max(maxSoFar, root.val)

            #check the left tree
            dfs(root.left, maxSoFar)
            #if parent and root is less than the parent
            #check the right tree
            dfs(root.right, maxSoFar)

        dfs(root, root.val)
        return res
            
