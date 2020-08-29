class Solution:
    def solve(self, start, end) -> bool:
        if (start,end) in self.dp:
            return self.dp[start,end]
        if end-start == 2:
            return max(self.piles[start], self.piles[end])
        parity = end-start %2
        if parity:
            score = max(self.piles[start] + self.solve(start+1,end), self.piles[end] + self.solve(start, end-1))
        else:
            score = max(self.solve(start+1,end), self.solve(start, end-1))
        self.dp[start,end] = score
        return score
        
    def stoneGame(self, piles: List[int]) -> bool:
        self.piles = piles
        self.dp = {}
        minstones = self.solve(0, len(piles)-1)
        print(minstones, sum(piles)//2)
        if minstones > sum(piles)//2:
            return True
        else:
            return False
