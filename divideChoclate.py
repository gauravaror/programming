class Solution:
    def solve(self, i, K):
        if (i,K) in self.dp:
            return self.dp[i,K]
        if K != 0 and i >= len(self.sweetness)-1:
            return -float('inf')
        if K == 0:
            return sum(self.sweetness[i:])
        mina = 0
        for j in range(i, len(self.sweetness) - 1):
            thiscut = min(sum(self.sweetness[i:j+1]), self.solve(j+1, K-1))
            if thiscut != -float('inf'):
                mina = max(mina, thiscut)
        self.dp[i,K] = mina
        return mina
        
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        self.sweetness = sweetness
        self.dp = {}
        return self.solve(0,K)
