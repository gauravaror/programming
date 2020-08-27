# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def dfs(self, root):
        if not root:
            return "None"
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        rep = '(' + left + ')'+ str(root.val) + '(' + right  +')'
        self.tracer[rep].append(root)
        return rep
        
        
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.tracer = defaultdict(list)
        self.dfs(root)
        output = []
        for i in self.tracer.keys():
            if len(self.tracer[i]) > 1:
                output.append(self.tracer[i][0])
                
        return output
