class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        dp = [False]*(2**k)
        all_one = (1<<k) - 1
        has = 0
        got = 2**k
        for i,l in enumerate(s):
            has = ((has<<1) & all_one) | int(l)
            if i >= k-1 and dp[has] == False:
                dp[has] = True
                got -= 1
                if got == 0:
                    return True
        return False 
