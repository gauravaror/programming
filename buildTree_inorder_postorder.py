# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        if len(inorder) == 0:
            return None
            
        parent = postorder[-1]
        inParentIndex = inorder.index(parent)
        left = inParentIndex
        right = inParentIndex + 1
        inleft = inorder[:left]
        inright = inorder[right:]
        
        postleft = postorder[:left]
        postright = postorder[left:len(postorder)-1]
        #print(parent, inleft, inright, postleft, postright)
        leftTree = self.buildTree(inleft, postleft)
        rightTree = self.buildTree(inright, postright)
        return TreeNode(parent, leftTree, rightTree)
