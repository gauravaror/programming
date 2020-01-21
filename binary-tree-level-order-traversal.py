# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        answer = []
        stack = []
        current_level = 0
        if not root:
            return []
        stack.append((root,1))
        while len(stack) > 0:
            #print(stack)
            elem = stack.pop(0)
            level = elem[1]
            node = elem[0]
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
            if current_level != level:
                answer.append([])
                current_level = level
            answer[-1].append(node.val)
        return answer
