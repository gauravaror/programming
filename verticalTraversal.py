# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        stack = [(root, 0, 0)]
        dd = defaultdict(list)
        mmin = float('inf')
        mmax = -float('inf')
        lh, lw = 0,0
        while len(stack) > 0:
            elem, h, w = stack.pop(0)
            if elem.left:
                stack.append((elem.left, h+1, w-1))
            if elem.right:
                stack.append((elem.right, h+1, w+1))
            mmin = min(mmin, w)
            mmax = max(mmax, w)
            print(dd[w], elem, h, w)
            #if len(dd[w]) > 0  and dd[w][-1][1] == h and dd[w][-1][2] == w and dd[w][-1][0] > elem.val:
            idx = len(dd[w])
            while len(dd[w]) > 0 and idx >= 1 and dd[w][idx-1][2] == w and dd[w][idx-1][1] == h and dd[w][idx-1][0] > elem.val:
                idx -= 1
            dd[w].insert(idx, (elem.val,h, w))
            #else:
                #dd[w].append((elem.val,h, w))
        print(dd, mmin, mmax)
        output = []
        for i in range(mmin, mmax+1):
            output.append([])
            for j in dd[i]:
                output[-1].append(j[0])
        return output
