# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#time O(N), must visit every node
#space O(N), recursive call stack

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                #return true its balanced, and level is 0
                return [True, 0]
            #recurse left and right
            left, right = dfs(root.left), dfs(root.right)
            #check balancing conditions
            #left true, right true, difference between two less than 1
            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)
            #pass balanced status and one plus max depth of left and right 
            # because we are moving one level deeper
            return [balanced, 1+max(left[1], right[1])]
        #return 
        return dfs(root)[0]