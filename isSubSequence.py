class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        if lens == 0:
            return True
        if lent == 0:
            return False
        dp = [[0]*lens for _ in range(lent)]
        for i in range(lens):
            dp[0][i] = 1 if (s[i] == t[0]) else 0
        dp[0][0] = 1 if (t[0] == s[0]) else 0
        for o in range(1, lent):
            matched = False
            for i in range(lens):
                if i > 0:
                    newdp = max(dp[o-1][i], dp[o][i-1])
                else:
                    newdp = dp[o-1][i]
                if t[o] == s[i]:
                    if not matched:
                        newdp += 1
                        matched = True
                    
                dp[o][i] = newdp
        print(dp)
        return dp[len(t)-1][lens-1] == len(s)
