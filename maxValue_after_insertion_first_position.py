class Solution:
    def maxValue(self, n: str, x: int) -> str:
        start = 0
        end = len(n)
        if n[0] == '-':
            start = 1
        idx = start
        while idx < end:
            if start == 0 and int(n[idx]) < x:
                break
            if start == 1 and int(n[idx]) > x:
                break
            idx += 1
        return n[:idx] + str(x) + n[idx:]
        
