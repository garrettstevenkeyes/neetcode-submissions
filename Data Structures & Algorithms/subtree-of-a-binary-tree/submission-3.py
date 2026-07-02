# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #define helper function, two root inputs
        def helper(rootA, rootB):
            #if they both dont exist return true
            if not rootA and not rootB:
                return True

            #if one exists and the other doesnt return false
            if (rootA and not rootB) or (not rootA and rootB):
                return False

            if (rootA.val != rootB.val):
                return False

            #recurse
            return helper(rootA.left, rootB.left) and helper(rootA.right, rootB.right)
        
        if not subRoot:
            return True

        # empty root cannot contain non-empty subRoot
        if not root:
            return False

        # either it matches here, or somewhere below
        return (
            helper(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )