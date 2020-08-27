# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_same(self, elem1, elem2):
        print("Same", elem1, elem2)
        if elem1 == None and elem2 == None:
            return True
        if elem1 == None or elem2 == None:
            return False
        if elem1.val != elem2.val:
            return False
        if self.is_same(elem1.left, elem2.left) and self.is_same(elem1.right, elem2.right):
            return True
        else:
            return False
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        stack = [root]
        dp = collections.defaultdict(list)
        output = []
        while len(stack) > 0:
            elem = stack.pop()
            any_same  = False
            if elem.val in dp:
                for l in dp[elem.val]:
                    same = self.is_same(l, elem)
                    if same:
                        any_same = True
                
                    print("Same 1 ", l, elem, same)
                    if same:
                        output.append(l)
                        continue
            if any_same:
                continue
            if elem.left:
                stack.append(elem.left)
            if elem.right:
                stack.append(elem.right)
            dp[elem.val].append(elem)
        return output
