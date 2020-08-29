# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delHelper(self, root, to_delete, parent, left=True):
        output = []
        if root:
            if root.val in to_delete:
                fag1 = self.delHelper(root.left, to_delete, None)
                fag2 = self.delHelper(root.right, to_delete, None)
                output.extend(fag1)
                output.extend(fag2)
                if parent:
                    if left:
                        parent.left = None
                    else:
                        parent.right = None

            else:
                fag1 = self.delHelper(root.left, to_delete, root)
                fag2 = self.delHelper(root.right, to_delete, root, False)
                output.extend(fag1)
                output.extend(fag2)
                if parent == None:
                    output.append(root)
                
        return output
        
    
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        output = self.delHelper(root, to_delete, None)
        #output.append(root)
        return output
                    
