# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxp(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            if root.val > self.maximum:
                self.maximum = root.val
            return root.val
        left_t = 0
        right_t = 0
        if root.right:
            right_t = self.maxp(root.right)
        if root.left:
            left_t = self.maxp(root.left)
        thi_val = root.val + right_t + left_t
        self.maximum  = max(self.maximum,root.val + right_t, root.val + left_t, root.val, root.val+right_t+left_t)
        return max(root.val + right_t, root.val + left_t, root.val)
        
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = -float('inf')
        if not root:
            return -2147483648
        self.maxp(root)
        return self.maximum
