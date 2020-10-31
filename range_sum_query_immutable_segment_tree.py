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
            node.val = value
            return node
        if node.mid >= index:
            node.left_ = self.insert(node.left(), index, value)
        else:
            node.right_ = self.insert(node.right(), index, value)
        node.val = self.merge(node.left(), node.right())
        return node
    
    def query(self, node, start, end):
        print(node.range_left, node.range_right, start, end)
        if node.range_right < start or node.range_left > end:
            return 0
        if node.range_left == node.range_right or (node.range_right <= end and node.range_left >= start):
            return node.val
        if start > node.mid:
            return self.query(node.right(), start, end)
        if end <= node.mid:
            return self.query(node.left(), start, end)
        return self.query(node.left(), start, node.mid) +  self.query(node.right(), node.mid+1, end)
        
class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(len(nums))
        
        for idx,i in enumerate(nums):
            self.segment_tree.insert(self.segment_tree.root, idx, i)
        print(str(self.segment_tree.root))
    def sumRange(self, i: int, j: int) -> int:
        return self.segment_tree.query(self.segment_tree.root, i, j)
    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
