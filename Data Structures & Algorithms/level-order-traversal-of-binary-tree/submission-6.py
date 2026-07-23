# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #return none if not root
        if not root: return []
        #create empty heap with root
        currLvl = [root]
        res = []
        #while its not empty iterate
        while currLvl:
            curr = []
            nxtLvl = []
            for node in currLvl:
                curr.append(node.val)
                if node.left:
                    nxtLvl.append(node.left)
                if node.right:
                    nxtLvl.append(node.right)
            res.append(curr)
            curr = []
            currLvl = nxtLvl
            nxtLvl = []
        
        return res
            
            


