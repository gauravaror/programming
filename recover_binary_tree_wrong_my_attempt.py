from copy import copy
class Solution:
    def fixTree(self, node, low=-float('inf'), high=float('inf')):
        if not node:
            return
        if node.val < low:
            return node
        if node.val > high:
            return node
        ll = self.fixTree(node.left, low, node.val)
        rr = self.fixTree(node.right, node.val, high)
        if ll and rr:
            ll.val,rr.val = rr.val, ll.val
            return
        if ll and ll.val > node.val:
            ll.val,node.val = node.val, ll.val
            return
        elif rr and rr.val < node.val:
            rr.val,node.val = node.val, rr.val
            return
        return ll or rr            
        
    def recoverTree(self, root: TreeNode) -> None:
        self.fixTree(root)

