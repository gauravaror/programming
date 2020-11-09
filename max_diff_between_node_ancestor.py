# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterate_anscestor(self, root, mina, maxa):
        if not root:
            return
        mina = min(root.val, mina)
        maxa = max(root.val, maxa)
        thisdiff = abs(maxa-mina)
        if thisdiff > self.ans:
            self.ans = thisdiff
        self.iterate_anscestor(root.left, mina, maxa)
        self.iterate_anscestor(root.right, mina, maxa)
        return
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        self.iterate_anscestor(root, root.val, root.val)
        return self.ans
