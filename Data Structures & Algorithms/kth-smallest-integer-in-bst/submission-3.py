# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #assign k to class so it can be accessed
        #same with the ans
        self.k = k
        self.ans = None

        #define inorder 
        def inorder(node):
            
            # if there is no node or we have an aswer return 
            if not node or self.ans is not None:
                return
            #traverse left
            inorder(node.left)
            #after left traversals
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.ans