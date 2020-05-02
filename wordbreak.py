class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hh = {}
        for i in wordDict:
            hh[i] = True
        dp = [False]*(len(s) +1)
        dp[0] = True
        last_broken=0
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in hh:
                    dp[i] = True
                    last_broken = i
        return dp[-1]
### From https://leetcode.com/problems/word-break-ii/discuss/44368/Python-easy-to-understand-solution-(DP%2BDFS%2BBacktracking).
