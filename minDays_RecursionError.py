class Solution:
    def minDays(self, n: int) -> int:
        self.cache = {}
        def back(n):
            if n == 0:
                return 0
            if n in self.cache:
                return self.cache[n]
            
            out1 = 1 + back(n-1)
            if n % 2 == 0:
                out1 = min(1 + back(n/2), out1)
            if n%3 == 0:
                out1 = min(1+back(n - 2*(n/3)), out1)
            self.cache[n] = out1
            return out1
        return back(n)
