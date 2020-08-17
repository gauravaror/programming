# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        stack = [(0,root, 'root')]
        currlevel = 0
        levelnodes = 0
        hh = {'root': True}
        missingright = False
        nec = 'root'
        while len(stack) > 0:
            level, item, parent = stack.pop(0)
            if level == currlevel:
                levelnodes += 1
            else:
                print(levelnodes, 2**currlevel)
                if levelnodes != 2**currlevel:
                    return False
                levelnodes = 1
                currlevel = level
                nec = -1
            print('nect', nec, parent)
            if nec == -1:
                nec = parent
            elif nec == parent:
                nec = -1
            else:
                return False
                
            if item.right and not item.left:
                return False
            if item.left:
                stack.append((level+1, item.left, item.val))
            if item.right:
                stack.append((level+1, item.right, item.val))
            if not item.right:
                missingright = True
            if parent in hh:
                del hh[parent]
            else:
                hh[parent] = True
        if len(hh) > 1:
            return False
        else:
            return True
