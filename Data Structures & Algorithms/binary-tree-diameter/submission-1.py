# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # define result
        self.res = 0

        #define dfs, takes current node
        def dfs(curr):
            #if not curr node return 0
            if not curr:
                return 0

            #go all the way to the left and the right
            left = dfs(curr.left)
            right = dfs(curr.right)

            #get the max distance between the left and right
            self.res = max(self.res, left + right)
            #add 1 for the root
            return 1 + max(left, right)
        #call the recursion
        dfs(root)
        #return the result
        return self.res
