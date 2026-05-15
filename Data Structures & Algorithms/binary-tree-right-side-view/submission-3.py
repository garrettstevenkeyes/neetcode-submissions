# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 1. if not root return none
        if not root: return []
        # 2. create res list, next level list
        res = []
        nodeList = [root]
        # 3. for each item in the stack
        # create current lvl list,
        # pop item, add to curent lvl list, if left or right nodes add to next level list
        while nodeList:
            curLvl = []
            nxtLvl = []

            for _ in range(len(nodeList)):
                node = nodeList.pop(0)
                curLvl.append(node.val)

                if node.left: nxtLvl.append(node.left)
                if node.right: nxtLvl.append(node.right)

            res.append(curLvl[-1])
            curLvl = []
            nodeList = nxtLvl
            nxtLvl = []

        return res
            
