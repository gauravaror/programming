class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        ps = [0]*(len(stoneValue)+1)
        for i in range(1,len(stoneValue)+1):
            ps[i] = ps[i-1] + stoneValue[i-1]
        #print(ps)
        dp = [[-1]*(len(stoneValue)+2) for i in range((len(stoneValue)+2))]
        def dpa(l, r):
            #print(l,r)
            if dp[l][r] != -1:
                return dp[l][r]
            if l == r:
                dp[l][r] = 0
                return 0
            ma = 0
            for i in range(l, r):
                la = ps[i] - ps[l-1]
                ra = ps[r] - ps[i]
                #print(i, l, r, la, ra)
                if la > ra:
                    ma = max(ma, ra + dpa(i+1, r))
                elif la == ra:
                    ma = max(ma, la + dpa(i+1, r), la + dpa(l,i))
                else:
                    ma = max(ma, la + dpa(l, i))
            dp[l][r] = ma
            #print(l, r, ma)
            return ma
        dpa(1, len(stoneValue))
        #print(dp)
        return dp[1][len(stoneValue)]
