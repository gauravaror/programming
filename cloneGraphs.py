"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.clones = {}
        self.seen = {}
        
    def cloneGraph1(self, node:'Node') -> 'Node':            
        nn = []
        if node.val in self.clones:
            return self.clones[node.val]
        else:
            self.clones[node.val] = Node(node.val, [])
        
        if node.neighbors:
            for n in node.neighbors:
                if n.val not in self.clones:
                    cl = self.cloneGraph1(n)
                    self.clones[n.val] = cl
                nn.append(self.clones[n.val])
        out = self.clones[node.val]
        out.neighbors = nn
        self.clones[node.val] = out
        return out
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        output = self.cloneGraph1(node)
        return output
