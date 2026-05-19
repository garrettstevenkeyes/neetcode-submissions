# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, treeNodeA, treeNodeB):
        if not treeNodeA and not treeNodeB:
            return True

        if (treeNodeA and not treeNodeB) or (not treeNodeA and treeNodeB):
            return False
        
        if treeNodeA.val != treeNodeB.val:
            return False

        return self.isSameTree(treeNodeA.left, treeNodeB.left) and self.isSameTree(treeNodeA.right, treeNodeB.right)

    
