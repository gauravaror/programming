# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, output):
        if not root:
            return
        if root.left:
            self.dfs(root.left, output)
        output.append(root.val)
        if root.right:
            self.dfs(root.right, output)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree1 = []
        self.dfs(root1, tree1)
        tree2 = []
        self.dfs(root2, tree2)
        if len(tree1) == 0:
            return tree2
        if len(tree2) == 0:
            return tree1
        output = []
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(tree1) and pointer2 < len(tree2):
            if tree1[pointer1] < tree2[pointer2]:
                output.append(tree1[pointer1])
                pointer1 += 1
            else:
                output.append(tree2[pointer2])
                pointer2 += 1
        if pointer1 < len(tree1):
            output.extend(tree1[pointer1:])
        if pointer2 < len(tree2):
            output.extend(tree2[pointer2:])
        return output
