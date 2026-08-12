"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy_map = {}
        def dfs(node):
            if node in copy_map:
                return copy_map[node]

            copy = Node(node.val)
            copy_map[node] = copy

            for nei in node.neighbors:
                next = dfs(nei)
                copy.neighbors.append(next)
            
            return copy
        return dfs(node) if node else None




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

