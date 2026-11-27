# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        curr_level = [root]
        while curr_level:
            curr = []
            nxt = []
            for node in curr_level:
                curr.append(node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            
            res.append(curr)
            curr_level = nxt

        return res

