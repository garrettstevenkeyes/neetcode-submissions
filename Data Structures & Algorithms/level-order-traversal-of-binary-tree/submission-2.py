# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Plan
# 1. if not root return none
# 2. create current level list, next level list
# 3. for each item in the stack
# create current lvl list,
# pop item, add to curent lvl list, if left or right nodes add to next level list
# 4. set current level = next level and reset next level 
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. if not root return none
        if not root: return []
        # 2. create res list, next level list
        res = []
        queue = deque()
        queue.append(root)
        # 3. for each item in the stack
        # create current lvl list,
        # pop item, add to curent lvl list, if left or right nodes add to next level list
        while queue:
            curLvl = []
            nxtLvl = deque()

            for _ in range(len(queue)):
                node = queue.popleft()
                curLvl.append(node.val)

                if node.left: nxtLvl.append(node.left)
                if node.right: nxtLvl.append(node.right)

            res.append(curLvl)
            curLvl = []
            queue = nxtLvl
            nxtLvl = []

        return res
            
        # 4. set current level = next level and reset next level 

