# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        count = 0
        while True:
            while root:
                stack.append(root)
                root = root.left
            elem = stack.pop()
            count += 1
            if count == k:
                return elem.val
            root = elem.right
