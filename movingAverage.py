class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.current_sum = 0
        self.size = size
        
        

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.queue.appendleft(val)
            self.current_sum += val
        else:
            elem = self.queue.pop()
            self.queue.appendleft(val)
            self.current_sum += val
            self.current_sum -= elem
        return self.current_sum/len(self.queue)
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
