# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_longest(self, node) -> int:
        right_length = -float('inf')
        left_length = -float('inf')
        total_length = 0
        if node.right == None and node.left == None:
            if self.longest_path < 1:
                self.longest_path = 1
            return 1
            
        if node.right:
            right_length = self.find_longest(node.right)
            total_length += right_length
            
        if node.left:
            left_length = self.find_longest(node.left)
            total_length += left_length
        
        total_length += 1
        
        if total_length > self.longest_path:
            self.longest_path = total_length
        ml = max(right_length, left_length)
        print("longest path", ml, right_length, left_length)
        if ml == -float('inf'):
            return 0
        else:
            return ml + 1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.longest_path = -float('inf')
        self.find_longest(root)
        return self.longest_path -1
