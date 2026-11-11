"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict 
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #init a dictionary to store relationships in
        oldToNew = {}
        #create traversal func
        def dfs(node):
            #base case, if not node return 
            if not node: return None

            #check if we have seen the node before
            if node in oldToNew:
                return oldToNew[node]
            
            #copy the node
            copy = Node(node.val)

            #save the node into the dictionary
            oldToNew[node] = copy

            #otherwise go through the neighbors
            for nei in node.neighbors:
                #save the neighbor copy
                neighbor_copy = dfs(nei)
                #put to neighbor list for copy
                copy.neighbors.append(neighbor_copy)
                
            return copy
        return dfs(node)