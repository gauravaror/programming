# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, le: int, k:int):
        print("sada", root.val, le,k)
        if root.left:
            le = self.dfs(root.left,le,k)
        if le == -1:
            return -1
        le += 1
        if le == k:
            print("Found", le, k, root.val)
            self.ans = root.val
            return -1
        print("continueing", le)
        if le == -1:
            return -1
        print("continueing1111", le)
        re = le
        if root.right:
            re = self.dfs(root.right, le, k)
        return re
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.dfs(root, 0, k)
        return self.ans
