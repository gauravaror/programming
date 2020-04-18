import math
from sys import stdin

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def solve(treelist):
    if len(treelist) == 0:
        return -1
    current = 0
    root = TreeNode(treelist[current])
    current += 1
    stack = [root]
    while len(stack) > 0:
        top_elem = stack.pop(0)
        if treelist[current] != -1:
            top_elem.left = TreeNode(treelist[current])
        current += 1
        if treelist[current] != -1:
            top_elem.right = TreeNode(treelist[current])
        current += 1
        stack.append(top_elem.left)
        stack.append(top_elem.right)
        if current >= len(treelist):
            break
    if not root:
        return -1
    if not root.left and not root.right:
        return 1
    ans = count_subtree(root)
    print(ans)
    if ans[0] != -1:
        return ans[1] + 1
    else:
        return ans[1]

def count_subtree(root):
    if not root:
        return -1,0
    if not root.left and not root.right:
        return root.val,1
    lval, lcount = count_subtree(root.left)
    rval, rcount = count_subtree(root.right)
    if lval == -1 or rval == -1:
        return -1, (lcount + rcount)
    if root.val == lval and root.val == rval:
        return root.val, (1 + lcount + rcount)
    else:
        return -1, (lcount + rcount)

def preorder(root):
    print(root)
    if root:
        print(root.val)
    if root == None:
        return '()'
    return str(root.val) + '(' + preorder(root.left) + ')(' + preorder(root.right) + ')'

def read_testcase():
    height = int(stdin.readline())
    treelist = []
    for level in range(height+1):
        this_level = stdin.readline()
        treelist.extend([ int(i) for i in this_level.split()])
    print(solve(treelist))
read_testcase()
