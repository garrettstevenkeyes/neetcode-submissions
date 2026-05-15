"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #map old node to new node
        oldToNew = {}
        #do dfs 
        def dfs(node):
            #if we have seen the node return it
            if node in oldToNew:
                return oldToNew[node]
            #copy the node
            copy = Node(node.val)
            #save the node into the dictionary
            oldToNew[node] = copy
            #iterate on main neighbors
            for nei in node.neighbors:
                #do the iteration
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None