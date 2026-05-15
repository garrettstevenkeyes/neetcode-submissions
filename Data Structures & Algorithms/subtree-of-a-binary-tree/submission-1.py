# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, t: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        #if not subtree return true
        if not s: return True
        #if not tree return False 
        if not t: return False

        #if its the same tree
        if self.sameTree(s, t):
            return True
        
        return (self.isSubtree(t.left, s) or
            self.isSubtree(t.right, s))


    def sameTree(self, s, t):
        #If there is no main and no sub tree
        if not s and not t:
            return True
        #if there is a subtree and a main tree and subtree root value equals main tree root val
        if s and t and s.val == t.val:
            # recurse left
            # recurse right
            return (self.sameTree(s.left, t.left) and 
                self.sameTree(s.right, t.right))
        #other cases return False
        return False

