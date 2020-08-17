# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = [(root, [])]
        ppath = None
        qpath = None
        while ppath == None or qpath == None:
            elem, parent  = queue.pop()
            parent.append(elem)
            #print(ppath, parent, qpath, elem.val, p.val, q.val)
            if elem.val == p.val:
                ppath = parent.copy()
            if elem.val == q.val:
                qpath = parent.copy()
            if elem.left:
                queue.append((elem.left, parent.copy()))
            if elem.right:
                queue.append((elem.right, parent.copy()))
        ind = 0
        #print(ppath, qpath)
        while ind < min(len(ppath), len(qpath)) and ppath[ind].val == qpath[ind].val:
            ind += 1
        return ppath[ind-1]
