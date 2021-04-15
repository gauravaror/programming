class Solution:
    def fib1(self, n):
        if n <= 1:
            return n
        if n in self.cache:
            return self.cache[n]
        ans = self.fib1(n-1) + self.fib1(n-2)
        self.cache[n] = ans
        return ans
    
    def fib(self, n: int) -> int:
        self.cache = {}
        return self.fib1(n)
        
        
