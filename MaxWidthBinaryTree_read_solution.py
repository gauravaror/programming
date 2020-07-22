# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        stack = []
        stack.append((root, 0, 1))
        level = 0
        width = 0
        left_most = 1
        while len(stack) > 0:
            celem, cur_level, nid = stack.pop(0)
            if celem and celem.left:
                stack.append((celem.left, cur_level + 1, 2*nid))
            
            if celem and celem.right:
                stack.append((celem.right, cur_level + 1, 2*nid + 1))

            if level != cur_level:
                level = cur_level
                left_most = nid
            width = max(width, nid - left_most + 1)
        return width
