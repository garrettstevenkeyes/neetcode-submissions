# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #init a res and k counter
        self.res = None
        self.k = k
        #def inorder helper
        def inorder(node):
            ##if not node or we have our answer assigned return 
            if not node or self.res != None:
                return
            #traverse left
            inorder(node.left)
            #subtract from k
            self.k -= 1
            #If our k equals the target
            if self.k == 0:
                #set it to our result
                self.res = node.val
            #traverse right
            inorder(node.right)
            
        #call it on our root
        inorder(root)
        return self.res