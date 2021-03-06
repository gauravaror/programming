# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        output = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                item = stack.pop()
                output.append(item.val)
                root = item.right
        return output
