class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count_ge = 1
        
class Solution:
    def insert(self, val, node):
        if node == None:
            return Node(val)
        elif node.val > val:
            node.left = self.insert(val, node.left)
        elif node.val == val:
            node.count_ge += 1
        else:
            node.count_ge += 1
            node.right = self.insert(val, node.right)
        return node
    
    def search(self, val, node):
        if node == None:
            return 0
        if node.val == val:
            return node.count_ge
        elif node.val > val:
            return node.count_ge + self.search(val, node.left)
        else:
            return self.search(val, node.right)
        
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) < 2:
            return 0
        bst = Node(nums[0])
        for i in nums[1:]:
            ans += self.search(2*i+1, bst)
            self.insert(i, bst)
        return ans
        
