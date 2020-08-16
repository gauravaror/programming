class Solution:
    def minDays(self, n: int) -> int:
        self.cache = {}
        def nextsteps(n):
            out = [n-1]
            if n%2 == 0:
                out.append(n/2)
            if n%3 == 0:
                out.append(n - 2*(n/3))
            return out
        def back(n):
            if n == 0:
                return 0
            if n in self.cache:
                return self.cache[n]
            out1 = n
            if n%3 == 0:
                out1 = min(out1, 1 + back(n//3))
            if n%3 == 1:
                out1 = min(out1, 2 + back(n//3))
            if n%3 == 2:
                out1 = min(out1, 3 + back(n//3))
            if n%2 == 0:
                out1 = min(1 + back(n//2), out1)
            if n%2 == 1:
                out1 = min(2 + back(n//2), out1)
            self.cache[n] = out1
            return out1
        back(n)
        print(self.cache)
        return self.cache[n]
