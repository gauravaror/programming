class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0]*(n+1)
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        t[1] = 1
        t[2] = 1
        for i in range(3, n+1):
            t[i] = t[i-1] + t[i-2] + t[i-3]
        return t[-1]
