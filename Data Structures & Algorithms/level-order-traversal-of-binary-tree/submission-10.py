# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        #early exit
        if not root:
            return res

        queue = [root]
        while queue:
            nextLevel = []
            currLevel = []

            for node in queue:
                currLevel.append(node.val)
                
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            
            res.append(currLevel)
            queue = nextLevel
        
        return res


            