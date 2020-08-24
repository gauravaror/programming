# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeaves(self, root: TreeNode, side: str) -> int:
        if not root.left and not root.right:
            if side == 'l':
                self.leftLeaves += root.val
            return
        if root.left:
            self.getLeaves(root.left, 'l')
        if root.right:
            self.getLeaves(root.right, 'r')
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.leftLeaves = 0
        self.getLeaves(root, '')
        return self.leftLeaves
