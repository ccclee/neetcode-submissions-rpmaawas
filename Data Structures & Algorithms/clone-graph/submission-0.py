"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        memo ={}

        def creatNode(node):
            if node and node not in memo :
                memo[node] = Node(node.val, [])
                for n in node.neighbors:
                    creatNode(n)
        
        creatNode(node)

        for old, new in memo.items():
            for oldn in old.neighbors:
                new.neighbors.append(memo[oldn])

        return memo[node] if node else None
        