class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def addNum(self, num: int) -> None:
        start = 0
        end = len(self.store) - 1
        mid = (start + end)//2
        while start < end:
            if (self.store[mid] > num):
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
        if mid < 0:
            mid = 0
        #print(mid)
        if mid < len(self.store) and self.store[mid] < num:
            mid += 1
            
        self.store.insert(mid, num)
        #print(self.store, num)
        

    def findMedian(self) -> float:
        if (slen := len(self.store)) % 2 == 0:
            return (self.store[slen // 2] + self.store[slen//2 - 1])/2
        else:
            return self.store[slen//2]
