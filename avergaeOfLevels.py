# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        len_ = defaultdict(int)
        sum_ = defaultdict(int)
        max_level = 0
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop(0)
            len_[level] += 1
            sum_[level] += node.val
            max_level = max(max_level, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        output = []
        for i in range(max_level + 1):
            if i in len_ and i in sum_:
                output.append(sum_[i] / len_[i])
        return output
