import random
class Solution:

    def __init__(self, w: List[int]):
        self.picker = []
        mi = min(w)
        w = [i//mi for i in w]
        for idx,i in enumerate(w):
            self.picker.extend([idx]*i)
        

    def pickIndex(self) -> int:
        return random.sample(self.picker,1)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
