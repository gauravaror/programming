# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseDepth(self, root: TreeNode, depth: int, parent: TreeNode):
        if self.x_d != None and self.y_d != None:
            return
        if not root:
            return
        if self.x == root.val:
            self.x_d = (depth+1, parent)
        if self.y == root.val:
            self.y_d = (depth+1, parent)
        if root.left:
            self.traverseDepth(root.left, depth+1, root)
        if root.right:
            self.traverseDepth(root.right, depth+1, root)
        
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x = x
        self.y = y
        self.x_d = None
        self.y_d = None
        self.traverseDepth(root, 0, None)
        print(self.x_d, self.y_d)
        if self.x_d[0] == self.y_d[0] and self.x_d[1].val != self.y_d[1].val:
            return True
        else:
            return False
