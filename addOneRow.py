# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def df(root, dep):
            if not root:
                return
            if dep == 2:
                nl = TreeNode(v)
                nr = TreeNode(v)
                nl.left = root.left
                nr.right = root.right
                root.left = nl
                root.right = nr
                return root
            else:
                root.left = df(root.left, dep-1)
                root.right = df(root.right, dep-1)
                return root
                
        if d == 1:
            r = TreeNode(v)
            r.left = root
            return r
        else:
            return df(root, d)
        
