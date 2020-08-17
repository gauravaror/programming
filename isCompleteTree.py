# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        st = [(root, 1)]
        total_nodes = 0
        last_elem = 1
        while len(st) > 0:
            item, v = st.pop(0)
            last_elem = v
            total_nodes += 1
            if item.left:
                st.append((item.left, 2*v))
            if item.right:
                st.append((item.right, 2*v+1))
        return total_nodes == last_elem 
