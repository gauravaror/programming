class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        start = 1
        diff = 0
        times = 1
        while times < 32:
            #print(start, x, y, x&start, y&start)
            if x&start != y&start:
                diff += 1
            start = start<<1
            times += 1
        return diff
