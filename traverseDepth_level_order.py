# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        stack = [(root, 0, None)]
        x_d = None
        y_d = None
        dd = float('inf')
        while len(stack) > 0:
            elem = stack.pop(0)
            #print(elem[0].val, elem[1], stack)
            if elem[0].val == x:
                x_d = (elem[1], elem[2])
                dd = elem[1]
            if elem[0].val == y:
                y_d = (elem[1], elem[2])
                dd = elem[1]
            if elem[1] > dd:
                break
            if elem[0].right:
                stack.append((elem[0].right, elem[1]+1, elem[0].val))
            if elem[0].left:
                stack.append((elem[0].left, elem[1]+1, elem[0].val))
        if x_d != None and y_d != None:
            if x_d[0] == y_d[0] and x_d[1] != y_d[1]:
                return True
            else:
                return False
        else:
            return False
