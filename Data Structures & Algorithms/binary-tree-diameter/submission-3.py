# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr):
            nonlocal res

            #define te base case
            if not curr:
                return 0

            #traverse left
            #get left distance
            left = dfs(curr.left)

            #traverse right
            #get right distance
            right = dfs(curr.right)

            res = max(res, left + right)

            return 1 + max(left, right)
        dfs(root)
        return res