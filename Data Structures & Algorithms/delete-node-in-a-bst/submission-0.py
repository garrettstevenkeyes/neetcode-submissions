# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #does the root exit
        if not root:
            return None

        #navigate to the node

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            #if it does exist check its children nodes
            #if the left exists and not the right
            #return left, vice versa for right
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # if both exist move right and switch values
                #then recurse on the value we moved
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)

        return root
        