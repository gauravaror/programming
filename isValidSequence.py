# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:        
        if len(arr) == 0:
            return False
        if root.val == arr[0]:
            if not root.left and not root.right and len(arr) == 1:
                return True
            right = False
            left = False
            if root.right:
                right = self.isValidSequence(root.right,arr[1:])
            if root.left:
                left = self.isValidSequence(root.left, arr[1:])
            return (right | left)
        else:
            return False
