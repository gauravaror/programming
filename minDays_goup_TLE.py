class Solution:
    def minDays(self, n: int) -> int:
        self.cache = {0:0}
        def daypred(g):
            mina = self.cache[g-1]
            if g %2 == 0:
                mina = min(mina, self.cache[g/2])
            if g %3 == 0:
                mina = min(mina, self.cache[g- 2*(g/3)])
            self.cache[g] = 1 + mina
            return mina
        for i in range(1, n+1):
            daypred(i)
        return self.cache[n]
