# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isuni(self, root:TreeNode, val):
        if not root:
            return True
        l = self.isuni(root.left, val)
        r = self.isuni(root.right, val)
        if root.val == val and l and r:
            return True
        return False
    
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isuni(root, root.val)
