# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def ps(self, root: TreeNode, cum, dic) -> int:
        #print(dic, cum)
        if not root:
            return
        cum += root.val
        remaining = cum-self.sum
        if remaining in dic:
            #print(remaining, dic)
            self.paths += dic[remaining]
        dic1 = dic.copy()
        dic1[cum] += 1
        if root.left:
            self.ps(root.left, cum, dic1)
        if root.right:
            self.ps(root.right, cum, dic1)
            
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.sum = sum
        self.paths = 0
        c = Counter()
        c[0] = 1
        self.ps(root, 0, c)
        return self.paths
