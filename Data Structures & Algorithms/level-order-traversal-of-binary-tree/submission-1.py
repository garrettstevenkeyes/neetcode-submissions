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
        queue = deque([root])
        # add our root to the queue
        res = []
        while queue:
            level = []
            nextLevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                #get current node and add it to the level
                level.append(node.val)
                #if it has children add them to the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res 

