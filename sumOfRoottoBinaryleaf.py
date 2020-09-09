# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumHelper(self, root, oldsum):
        if not root:
            return
        if not root.left and not root.right:
            self.sum += 2*oldsum + root.val
            return
        self.sumHelper(root.left, 2*oldsum + root.val)
        self.sumHelper(root.right, 2*oldsum + root.val)
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.sum = 0
        self.sumHelper(root, 0)
        return self.sum
