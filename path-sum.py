# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return 0
        stack = [(root,0)]
        while len(stack) > 0:
            current_node = stack.pop()
            leaf_node = True
            sum_here = current_node[1] + current_node[0].val
            #print(current_node[0].left != None)
            if current_node[0].left != None:
                leaf_node = False
                stack.append((current_node[0].left, sum_here))
            if current_node[0].right != None:
                leaf_node = False
                stack.append((current_node[0].right, sum_here))
            #print("Val", current_node[0], leaf_node)
            if leaf_node:
                #print(current_node[1], current_node[0])
                if (current_node[1] + current_node[0].val) == sum:
                    return True
        return False
