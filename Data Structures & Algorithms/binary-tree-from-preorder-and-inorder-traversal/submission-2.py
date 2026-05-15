# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # both are neeeded to merge
        # otherwise return None
        if not preorder or not inorder:
            return None
        # preorder means root first
        # get root
        root = TreeNode(preorder[0])
        #get index of mid point (root)
        mid = inorder.index(preorder[0])
        # left is preorder right of root to mid node
        # inorder to mid node
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # right is preorder after mid
        #inorder after mid
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
