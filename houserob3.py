# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, last_robbed, idx):
        if (idx,last_robbed)  in self.dp:
            return self.dp[idx, last_robbed]
        if not root:
            return 0
        if not last_robbed:
            ans =  max(self.solve(root.right, False, 2*idx+1) + self.solve(root.left, False, 2*idx), 
                       root.val + self.solve(root.left, True, 2*idx) + self.solve(root.right, True, 2*idx + 1))
        else:
            ans =  self.solve(root.left, False, 2*idx) + self.solve(root.right, False, 2*idx+1)
        
        self.dp[idx, last_robbed] = ans
        return ans
            
    def rob(self, root: TreeNode) -> int:
        self.dp = {}
        return max(self.solve(root, True, 1), self.solve(root, False, 1))
