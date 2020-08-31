# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def setNode(self, node, parent, left):
        if not parent:
            self.root = node
        elif left:
            parent.left = node
        else:
            parent.right = node

    def mergeNodes(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        if node1.val < node2.val:
            node1.right = self.mergeNodes(node1.right, node2)
            return node1
        else:
            node2.right = selr.mergeNodes(node2.right, node1)
            return node2
        
    def delNode(self, root, parent, left=True):
        if not root:
            return
        if root.val == self.key:
            if not root.left and not root.right:
                self.setNode(None, parent, left)
            else:
                mergedNode = self.mergeNodes(root.left, root.right)
                self.setNode(mergedNode, parent, left)
        else:
            if root.left:
                self.delNode(root.left, root)
            if root.right:
                self.delNode(root.right, root, left=False)
                
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self.root = root
        self.key = key
        self.delNode(root, None)
        return self.root
