class Node:
    def __init__(self, rleft, rright):
        self.range_left = rleft
        self.range_right = rright
        self.val = 0
        self.mid =  (self.range_left + self.range_right)//2
        self.right_, self.left_ = None, None
    
    def left(self):
        return self.left_ or Node(self.range_left, self.mid)
    
    def right(self):
        return self.right_  or Node(self.mid +1, self.range_right)
        
    def __str__(self):
        return str(self.val) + " | " +  str(self.left_) + " | " + str(self.right_)
    
class SegmentTree:
    def __init__(self, length):
        self.root = Node(0, length - 1)
    
    def merge(self, left, right):
        return left.val + right.val
    
    def insert(self, node, index, value):
        if node.range_left == node.range_right:
            node.val += value
            return node
        if node.mid >= index:
            node.left_ = self.insert(node.left(), index, value)
        else:
            node.right_ = self.insert(node.right(), index, value)
        node.val = self.merge(node.left(), node.right())
        return node
    
    def query(self, node, start, end):
        #print(node.range_left, node.range_right, start, end)
        if node.range_right < start or node.range_left > end:
            return 0
        if node.range_left == node.range_right or (node.range_right <= end and node.range_left >= start):
            return node.val
        if start > node.mid:
            return self.query(node.right(), start, end)
        if end <= node.mid:
            return self.query(node.left(), start, end)
        return self.query(node.left(), start, node.mid) +  self.query(node.right(), node.mid+1, end)
        

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        #print("ins", instructions)
        ma = max(instructions)
        c = Counter()
        segTree = SegmentTree(ma+1)
        cost = 0
        for idx,i in enumerate(instructions):
            less = segTree.query(segTree.root, 0, i-1)
            equal = c[i]
            #print("Less Equal", less, equal, cost)
            cost += min(less, idx-less-equal)
            segTree.insert(segTree.root, i, 1)
            c[i] += 1
        return cost % (10**9 + 7)


