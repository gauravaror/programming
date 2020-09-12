class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window_size = size
        self.current = 0
        self.queue = deque()
        

    def next(self, val: int) -> float:
        self.current += val
        self.queue.append(val)
        if len(self.queue) > self.window_size:
            ritem = self.queue.popleft()
            self.current -= ritem
        return self.current/len(self.queue)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
