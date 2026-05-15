"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #create a dictionary to map the old to the new
        oldToNew = {}
        
        #define a dfs function
        #it takes a node as input
        def dfs(node):
            #if the node is in our old to new map return it
            if node in oldToNew:
                return oldToNew[node]
            #if not create a copy
            copy_node = Node(node.val)
            #save it into our dictionary
            oldToNew[node] = copy_node
            #map neighbors
            #for each of the neighbors of the og node
            for nei in node.neighbors:
                #do the dfs on it
                copy_node.neighbors.append(dfs(nei))
            return copy_node

        #do the dfs on the root node
        return dfs(node) if node else None

