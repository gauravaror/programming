class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head = None
        self.tail = None
        self.hh = {}
        for i in nums:
            self.d_add(i)

    def showFirstUnique(self) -> int:
        if self.head == None:
            return -1
        else:
            return self.head.val
        

    def add(self, value: int) -> None:
        self.d_add(value)
        
    def d_add(self, value: int) -> None:
        if value in self.hh:
            if self.hh[value] != None:
                self.d_remove(self.hh[value])
                self.hh[value] = None
        else:
            nnode = Node(value)
            self.hh[value] = nnode
            if not self.head:
                self.head = nnode
                self.tail = nnode
            else:
                nnode.prev = self.tail
                self.tail.next = nnode
                self.tail = nnode
            
    def d_remove(self, node: Node) -> None:
        print("Remove", node.val, self.tail.val, self.head.val)
        if node == self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        if node == self.head:
            if not self.head.next:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        else:
            #prev = self.head.prev
            #nex = self.head.next
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            
        
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
