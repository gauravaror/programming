# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def get_successor(self, root):
        if not root.left:
            return None
        a = root.left
        while a.right:
            a = a.right
        return a
    
    def do_bst(self, root, smallest):
        if not root:
            return -1
        if root.val > smallest:
            succ = self.get_successor(root)
            if succ and succ.val >= smallest:
                return self.do_bst(root.left, smallest)
            else:
                return root.val
        elif root.val == smallest:
            return root.val
        else:
            if root.right:
                return self.do_bst(root.right, smallest)
            else:
                return -1
        
    def __init__(self, root: TreeNode):
        self.last_elem = 0
        self.root = root

    def next(self) -> int:
        #print("searching", self.last_elem)
        data = self.do_bst(self.root, self.last_elem)
        #print("found ", data)
        if data != -1:
            self.last_elem = data + 1
            return data

    def hasNext(self) -> bool:
        data = self.do_bst(self.root, self.last_elem)
        if data != -1:
            return True
        return False
        
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
