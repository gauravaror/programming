class Solution:
    def hammingWeight(self, n: int) -> int:
        lastbit = 1
        totalset = 0
        while n > 0:
            if n&lastbit:
                totalset += 1
            n = n >> 1
        return totalset
