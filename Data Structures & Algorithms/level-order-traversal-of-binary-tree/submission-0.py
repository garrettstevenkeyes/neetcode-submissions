# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # create a queue
        queue = [root]
        # add our root to the queue
        res = []
        while queue:
            level = []
            nextLevel = []
            for node in queue:
                #get current node and add it to the level
                level.append(node.val)
                #if it has children add them to the next level
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            
            res.append(level)
            queue = nextLevel
            level = []
            nextLevel = []
        return res 

