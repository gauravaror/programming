# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
import bisect
class Solution:
    def __init__(self):
        self.node = defaultdict(list)
        self.maxl = 0
        
    def explore(self, node, level):
        if not node and not level:
            return 0
        elif not node:
            return level
        if level:
            self.explore(node.left, level-1)
        else:
            level = self.explore(node.left, level)
        print(level, node.val)
        self.maxl = max(self.maxl, level)
        self.insert(level, node.val)
        self.explore(node.right, level+1)
        return level + 1
        
    def insert(self, level, val):
        idx = bisect.bisect_left(self.node[level], val)
        #self.node[level].insert(idx, val)
        self.node[level].append(val)
        
        
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.explore(root, None)
        print(self.maxl, self.node)
        output = []
        for i in range(self.maxl+1):
            output.append(self.node[i])
        return output
