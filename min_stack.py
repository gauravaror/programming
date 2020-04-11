class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ll = []
        self.min = []
        

    def push(self, x: int) -> None:
        #print("push", self.ll, self.min)
        self.ll.append(x)
        if len(self.min) > 0:
            curr_min = self.min[-1]
        else:
            curr_min = float('inf')
        if x < curr_min:
            self.min.append(x)
        else:
            self.min.append(curr_min)

    def pop(self) -> None:
        #print("pop", self.ll, self.min)
        if len(self.min) > 0:
            del self.min[-1]
            del self.ll[-1]

    def top(self) -> int:
        #print("top", self.ll, self.min)
        return self.ll[-1]
        

    def getMin(self) -> int:
        #print("Min", self.ll, self.min)
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
