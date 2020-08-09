class Solution:
    def __init__(self):
        self.cac = {}
        
    def getMin(self, start, end, cuts):
        s = str(start) + '_' + str(end)
        if s in self.cac:
            return self.cac[s]
        #print(start, end, cuts)
        if len(cuts) == 0:
            return 0
        mina = float('inf')
        ind = 0
        cost = end-start
        for idx,i in enumerate(cuts):
            tcost = self.getMin(start, cuts[idx], cuts[:idx]) + self.getMin(cuts[idx], end, cuts[idx+1:])
            mina = min(mina, tcost)
        self.cac[s] = cost + mina
        return cost + mina
            
        
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts)
        return self.getMin(0, n, cuts)

