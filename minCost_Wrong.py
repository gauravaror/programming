class Solution:
    def getMin(self, start, end, cuts):
        print(start, end, cuts)
        if len(cuts) == 0:
            return 0
        mina = float('inf')
        ind = 0
        cost = end-start
        for idx,i in enumerate(cuts):
            l,r = i-start, end-i
            thiscut = abs(l-r)
            if thiscut < mina:
                mina = thiscut
                ind = idx
        return cost + self.getMin(start, cuts[ind], cuts[:ind]) + self.getMin(cuts[ind], end, cuts[ind+1:])
            
        
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts)
        return self.getMin(0, n, cuts)
