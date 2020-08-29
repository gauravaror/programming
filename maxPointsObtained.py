class Solution:
    def solve(self, start, end, k):
        if (start,end,k) in self.dp:
            return self.dp[start,end,k]
        if k == 0:
            return 0
        if start > end:
            return 0
        maxa = max(self.cardPoints[start] + self.solve(start+1,end,k-1), self.cardPoints[end] + self.solve(start, end-1, k-1))
        self.dp[start,end,k] = maxa
        return maxa
        
        
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        print(len(cardPoints))
        self.cardPoints = cardPoints
        self.dp = {}
        return self.solve(0, len(cardPoints)-1, k)
