# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if not node:
            return []
        ans = self.inorder(node.left)
        if len(ans) > self.k:
            return ans
        ans.append(node.val)
        ans.extend(self.inorder(node.right))
        if len(ans) > self.k:
            return ans
        return ans
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        array = self.inorder(root)
        return array[k-1]
