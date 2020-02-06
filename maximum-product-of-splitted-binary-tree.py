# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
            left_tree = 0
            right_tree = 0
            if node.left:
                left_tree = self.dfs(node.left)
            if node.right:
                right_tree = self.dfs(node.right)
            left_prod = (self.total_sum-left_tree)
            left_prod *= left_tree
            right_prod = (self.total_sum-right_tree) 
            right_prod = right_prod*right_tree
            if (left_prod) > self.maximum:
                self.maximum = left_prod
            if right_prod > self.maximum:
                self.maximum = right_prod
            return (node.val + left_tree + right_tree) 

    def maxProduct(self, root: TreeNode) -> int:
        stack = []
        total_sum = 0
        stack.append(root)
        self.modulo = 1e9 + 7
        while len(stack) > 0:
            elem = stack[0]
            stack.pop(0)
            total_sum = total_sum +  (elem.val)
            if elem.left:
                stack.append(elem.left)
            if elem.right:
                stack.append(elem.right)
        self.maximum = 0
        self.total_sum = total_sum 
        self.dfs(root)
            
        print(total_sum, self.maximum)
        return int(self.maximum % self.modulo) 
