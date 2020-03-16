class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.arr = []
        

    def push(self, x: int) -> None:
        if len(self.arr) < self.max_size:
            self.arr.append(x)
            
    def pop(self) -> int:
        if len(self.arr) > 0:
            item = self.arr.pop()
            return item
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        if len(self.arr) <= k:
            for i in range(len(self.arr)):
                self.arr[i] = self.arr[i] + val
        else:
            for i in range(0, k):
                self.arr[i] = self.arr[i] + val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
