# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        rootval  = preorder[0]
        right_index = None
        for idx,i in enumerate(preorder[1:], 1):
            if i > rootval:
                right_index = idx
                break
        if right_index:
            print(rootval, right_index , preorder[1:right_index], preorder[right_index:])
            leftTree = self.bstFromPreorder(preorder[1:right_index])
            rightTree = self.bstFromPreorder(preorder[right_index:])
            root = TreeNode(rootval)
            root.left = leftTree
            root.right = rightTree
            return root
        else:
            root = TreeNode(rootval)
            root.left = self.bstFromPreorder(preorder[1:])
            return root
