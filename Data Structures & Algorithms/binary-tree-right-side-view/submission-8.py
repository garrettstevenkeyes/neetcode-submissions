# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #init a res
        res = []
        # define dfs (root, level)
        def dfs(root, level):
            #base case is if not root 
            if not root: 
                return
            
            #if our current level equals len of res we add it 
            #to result
            if level == len(res):
                res.append(root.val)

            #go right 
            dfs(root.right, level + 1)

            #go left
            dfs(root.left, level + 1)

            
        dfs(root, 0)
        return res
