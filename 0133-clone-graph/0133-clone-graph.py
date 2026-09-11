"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old = {}
        def dfs(node):
            if node in old:
                return old[node]

            temp = Node(node.val)
            old[node] = temp
            for neigh in node.neighbors:
                temp.neighbors.append(dfs(neigh))
            return temp
        
        return dfs(node)