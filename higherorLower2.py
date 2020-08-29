class Solution:
    def solve(self, start, end):
        if (start,end) in self.dp:
            return self.dp[(start,end)]
        mina = float('inf')
        if start >= end:
            return 0
        for i in range(start, end+1):
            mina = min(mina, max(self.solve(start, i-1) + i, i+self.solve(i+1,end)))
        self.dp[(start,end)] = mina
        return mina
    def getMoneyAmount(self, n: int) -> int:
        self.dp = {}
        return self.solve(1, n)
