import random
class Solution:

    def __init__(self, w: List[int]):
        self.picker = []
        acc = 0
        for i in w:
            acc += i
            self.picker.append(acc)
        
        

    def pickIndex(self) -> int:
        start = 0
        end = len(self.picker) - 1
        rs = random.randint(1, self.picker[-1])
        while start < end:
            mid = (start + end) //2
            if self.picker[mid] == rs:
                return mid
            elif self.picker[mid] < rs:
                start = mid + 1
            else:
                end = mid - 1
        if self.picker[start] < rs:
            return start + 1
        else: 
            return start

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
