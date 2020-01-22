# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root:
            return []
        answer = []
        stack = [(root,[])]
        while len(stack) > 0:
            current_node = stack.pop()
            leaf_node = True
            sum_here = current_node[1]
            sum_here.append(current_node[0].val)
            #print(current_node[0].left != None)
            #print("Sum", sum_here)
            if current_node[0].left != None:
                leaf_node = False
                stack.append((current_node[0].left, copy.copy(sum_here)))
            if current_node[0].right != None:
                leaf_node = False
                stack.append((current_node[0].right, copy.copy(sum_here)))
            #print(stack)
            if leaf_node:
                #print(current_node[1], current_node[0], sum_)
                if sum(sum_here) == sum_:
                    answer.append(sum_here)
        return answer
