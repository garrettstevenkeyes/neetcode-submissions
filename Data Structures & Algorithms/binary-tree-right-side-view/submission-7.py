# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # def dfs(root, depth)
        def dfs(root, depth):
            #if not root return up
            if not root:
                return 
            #if the depth equals the result length its at that level
            if depth == len(res):
                res.append(root.val)
            #go right
            dfs(root.right, depth + 1)
            #go left
            dfs(root.left, depth + 1)
            
        dfs(root,0)
        return res