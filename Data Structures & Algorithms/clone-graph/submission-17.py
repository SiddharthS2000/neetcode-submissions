"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldclone = {}
        if not node:
            return None

        def dfs(node):
            if node in oldclone:
                return oldclone[node]
            
            copy = Node(node.val)
            oldclone[node] = copy

            for nie in node.neighbors:
                copy.neighbors.append(dfs(nie))
            return copy
        
        return dfs(node)





        # oldtonew = {}

        # def dfs(node):
        #     if node in oldtonew:
        #         return oldtonew[node]

        #     copy = Node(node.val)
        #     oldtonew[node] = copy

        #     for nei in node.neighbors:
        #         next = dfs(nei)
        #         copy.neighbors.append(next)
        #     return copy

        # return dfs(node) if node else None         

