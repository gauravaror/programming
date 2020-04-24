class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.hh = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.capacity = capacity
        self.limit = 0
        
    def arrange_access(self, key: int) -> int:
        accessednode = self.hh[key]
        if self.tail != accessednode:
            prevn = accessednode.prev
            nextn = accessednode.next
            if prevn:
                prevn.next = nextn
            if nextn:
                nextn.prev = prevn
            if accessednode == self.head and nextn != None:
                self.head = nextn
            self.tail.next = accessednode
            accessednode.prev = self.tail
            self.tail = accessednode
        return accessednode.val
        

    def get(self, key: int) -> int:
        #print("get", key, self.head, self.tail, self.hh)
        if key in self.hh:
            return self.arrange_access(key)
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        #print("put", key,value, self.head, self.tail, self.hh)
        if key in self.hh:
            self.hh[key].val = value
            self.arrange_access(key)
        else:
            while self.limit >= self.capacity:
                remove_n = self.head
                del self.hh[remove_n.key]
                self.head = self.head.next
                self.limit -= 1
            newnode = Node(key, value)
            oldtail = self.tail
            oldtail.next  = newnode
            newnode.prev = oldtail
            self.tail = newnode
            self.hh[key] = newnode
            if self.limit == 0:
                self.head = newnode
            self.limit += 1
                
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
