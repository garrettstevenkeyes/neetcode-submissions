# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #if there is not a root return
        if not root:
            return []
        #root in list
        queue = [root]
        res = []
        #while that is not empty
        while queue:
            curr = []
            nxt = []
            #for every node in the list
            for node in queue:
                #add it to a curr list
                curr.append(node.val)
                #if there is a left child add it to next level
                if node.left:
                    nxt.append(node.left)
                #if there is a right child add it to next level
                if node.right:
                    nxt.append(node.right)

            #add the current level to the result
            res.append(curr)
            #make the current level the next level
            queue = nxt
            #reset the next level
            # nxt = []
            # curr = []
        #return the result
        return res