# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pre(self, root):
        if root.left:
            root = root.left
        else:
            return None
        while root.right:
            root = root.right
        return root.val
    
    def succ(self, root):
        if root.right:
            root = root.right
        else:
            return None
        while root.left:
            root = root.left
        return root.val
            
    def minDiffInBST(self, root: TreeNode) -> int:
        
        stack = [root]
        minDiff = float('inf')
        while len(stack) > 0:
            elem = stack.pop()
            pred_val = self.pre(elem)
            if pred_val:
                if elem.val - pred_val < minDiff:
                    minDiff = elem.val - pred_val 
            succ_val = self.succ(elem)
            if succ_val:
                if succ_val - elem.val < minDiff:
                    minDiff = succ_val - elem.val
            if elem.right:
                stack.append(elem.right)
            if elem.left:
                stack.append(elem.left)
        return minDiff
