class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = [0]
        def invert(s):
            g = s.copy()
            for i in range(len(g)):
                g[i] = 0 if g[i] == 1 else 1
            return g
        while len(s) < k:
            #print(s)
            g = invert(s)
            s.append(1)
            s.extend(g[::-1])
        #print(s)
        return str(s[k-1])
