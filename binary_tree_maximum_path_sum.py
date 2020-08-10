# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxpath = -float('inf')
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxi(root)     
        return self.maxpath
    
    def maxi(self, root:TreeNode ) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            self.maxpath = max(self.maxpath, root.val)
            return root.val
        leftval = 0
        rightval = 0
        if root.left:
            leftval = self.maxi(root.left)
        if root.right:
            rightval = self.maxi(root.right)
        self.maxpath = max(self.maxpath, root.val + leftval + rightval, root.val, root.val + leftval , root.val + rightval)
        return max(root.val, root.val+ leftval , root.val + rightval)
