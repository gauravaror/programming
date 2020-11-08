# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt1(self, root: TreeNode) -> (int, int):
        if not root:
            return (0,0)
        left = self.findTilt1(root.left)
        right = self.findTilt1(root.right)
        subtree_sum = left[0]+right[0] + root.val
        tilt_sum = abs(left[0]-right[0]) + left[1] + right[1]
        return (subtree_sum, tilt_sum)
    
    def findTilt(self, root: TreeNode) -> int:
        return self.findTilt1(root)[1]
        
