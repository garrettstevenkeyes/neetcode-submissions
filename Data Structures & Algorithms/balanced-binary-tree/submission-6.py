# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            #base case if not root its true, level 0
            if not root: return [True,0]
            #recurse left 
            left = dfs(root.left)
            #recurse right
            right = dfs(root.right)
            #check if left is true, right is true, and the level difference isnt bad
            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)

            return [balanced, 1+max(left[1], right[1])]

        return dfs(root)[0]