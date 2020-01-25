class Solution:
    def numTilings(self, N: int) -> int:
        
        g1 = 1
        g2 = 1
        g3 = 2
        if N == 1:
            ans = 1
        elif N == 2:
            ans = 2
        else:
            ans = 2
            for i in range(3, N+1):
                ans = ((2*g3 + g1) % (1e9 + 7))
                g1 = g2
                g2 = g3
                g3 = ans
                print(i, ans, g1, g2, g3)
        return int(ans % (1e9 + 7))
