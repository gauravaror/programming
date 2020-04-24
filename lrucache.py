class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = 0
        self.keylist = []
        self.hh = {}
        

    def get(self, key: int) -> int:
        if key in self.hh:
            self.keylist.remove(key)
            self.keylist.append(key)
            return self.hh[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hh:
            self.keylist.remove(key)
            self.keylist.append(key)
            self.hh[key] = value
        elif self.current < self.capacity:
            self.keylist.append(key)
            self.hh[key] = value
            self.current += 1
        else:
            topkey = self.keylist.pop(0)
            del self.hh[topkey]
            self.keylist.append(key)
            self.hh[key] = value
        #print(key, value, self.hh, self.keylist)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
