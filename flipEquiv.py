# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, root1, roo2) -> bool:
        if root1 == None and root2 == None:
            return True
        if root1  == None or root2 == None:
            return False
        if not root1.val == root2.val:
            return False
        leftsame = self.isSame(root1.left, roo2.left)
        rightsame = self.isSame(root1.right, roo2.right)
        return leftsame and rightsame

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if not root1.val == root2.val:
            return False
        ll = self.flipEquiv(root1.left, root2.left)
        lr = self.flipEquiv(root1.left, root2.right) 
        rl = self.flipEquiv(root1.right, root2.left)
        rr = self.flipEquiv(root1.right, root2.right) 
        return (ll or lr) and ( rl or rr)
