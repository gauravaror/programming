class Solution:
    def bt(self, cnums, left, allowed):
        if len(cnums) == self.k and left == 0:
            self.output.append(cnums)
            return
        if left == 0 or len(cnums) == self.k:
            return
        for i in range(allowed, 10):
            self.bt(cnums + [i], left-i, i+1)
        return
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.k = k
        self.output = []
        self.bt([], n, 1)
        return self.output
