# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #check if root 
        if not root:
            return []
        #init queue and res
        res = []
        stack = [root]
        #init next level
        
        #while queue not empty
        while stack:
            #init curr level
            curLvl = []
            nxtLvl = []
            #for each item in queue
            for node in stack:
                #add to current level
                curLvl.append(node.val)

                #if children add to next level
                if node.left:
                    nxtLvl.append(node.left)

                if node.right:
                    nxtLvl.append(node.right)

            
            #add curr level to res
            res.append(curLvl)
            curLvl = []
            stack = nxtLvl

        return res