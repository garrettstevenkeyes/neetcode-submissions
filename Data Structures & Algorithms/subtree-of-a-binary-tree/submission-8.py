# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(main_root, sub_root):
            if not main_root and not sub_root: return True
            if (not main_root and sub_root) or (main_root and not sub_root): return False
            if main_root.val != sub_root.val: return False
            return helper(main_root.left, sub_root.left) and helper(main_root.right, sub_root.right)

        if not root: return False
        if not subRoot: return True

        return (helper(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))