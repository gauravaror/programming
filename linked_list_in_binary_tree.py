# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree_height(self, root):
        if root == None:
            return 0
        left_height = self.tree_height(root.left)
        right_height = self.tree_height(root.right)
        return max(left_height, right_height) + 1
    
    def list_leng(self, he):
        if he == None:
            return 0
        return 1 + self.list_leng(he.next)
        
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if self.list_leng(head) > self.tree_height(root):
            return False
        return self.isSubPath1(head, root)
    
    def justMatchPath(self, head: ListNode, root: TreeNode) -> bool:
        if head == None:
            return True
        if root == None:
            return False
        if head.val == root.val:
            if self.justMatchPath(head.next, root.left):
                return True
            if self.justMatchPath(head.next, root.right):
                return True
        return False
        
    def isSubPath1(self, head: ListNode, root: TreeNode) -> bool:
        if head == None:
            return True
        if root == None:
            return False
        if root.val == head.val:
            left_mpath = self.justMatchPath(head.next, root.left)
            if left_mpath:
                return True
            right_mpath = self.justMatchPath(head.next, root.right)
            if right_mpath:
                return True
        left_path = self.isSubPath1(head, root.left)
        if left_path:
            return True
        right_path = self.isSubPath1(head, root.right)
        if right_path:
            return True
        return left_path or right_path
