import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def solve(tree):
    treelist = tree.split(',')
    print(treelist)
    levels = math.log(len(treelist))/math.log(2)
    current = 0
    root = TreeNode(treelist[current])
    current += 1
    stack = [root]
    while len(stack) > 0:
        top_elem = stack.pop(0)
        if treelist[current] != 'null':
            top_elem.left = TreeNode(treelist[current])
        current += 1
        if treelist[current] != 'null':
            top_elem.right = TreeNode(treelist[current])
        current += 1
        stack.append(top_elem.left)
        stack.append(top_elem.right)
        if current >= len(treelist):
            break
    all_leaf_k(root, 3)
    print("Answer", ans)

ans = []
def all_leaf_k(root, d):
    if not root.right and not root.left:
        print("Leaf", root.val)
        return 1, [root.val]
    print("Non Leaf", root.val)
    if root.right:
        right_d, right_leaf = all_leaf_k(root.right, d)
    else:
        right_d = 0
        right_leaf = []
    if root.left:
        left_d, left_leaf = all_leaf_k(root.left, d)
    else:
        left_d = 0
        right_leaf = []
    print("non leaf", root.val, right_d, left_d, left_leaf, right_leaf)
    if right_d + left_d == d and len(left_leaf) + len(right_leaf) > 0:
        right_leaf.extend(left_leaf)
        ans.append(right_leaf)
        right_leaf = []
        left_leaf = []
    elif right_d + left_d > d:
        if 2*(right_d - 1) < d and len(right_leaf) > 0:
            ans.append(right_leaf)
        if 2*(left_d - 1) < d and len(left_leaf) > 0:
            ans.append(left_leaf)
        left_leaf = []
        right_leaf = []
    left_leaf.extend(right_leaf)
    return max(left_d, right_d)+1, left_leaf


def preorder(root):
    print(root)
    if root:
        print(root.val)
    if root == None:
        return '()'
    return root.val + '(' + preorder(root.left) + ')(' + preorder(root.right) + ')'

solve("1,2,3,null,null,4,5")
ans = []
solve("4,2,6,1,3,5,7")
