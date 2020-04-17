# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        if not t.right and not t.left:
            return str(t.val)
        right = "(" + self.tree2str(t.right) + ")"
        left = "(" + self.tree2str(t.left) + ")"
        if t.left and not t.right:
            right = ""
        return str(t.val) + left + right
