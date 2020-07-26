class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(100):
            nn =  1<<i
            if n == nn:
                return True
        return False
