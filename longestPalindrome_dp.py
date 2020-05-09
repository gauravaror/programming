class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        max_len = 1
        start = 0
        end = 1
        for le in range(1, len(s)):
            for st in range(0, (len(s)-le)):
                if le == 1:
                    if s[st+le] == s[st]:
                        dp[st][st+le] = 1
                else:
                    #print(st, le, st+le, len(s), len(s)-le)
                    if dp[st+1][st+le-1] == 1 and s[st] == s[st+le]:
                        dp[st][st+le] = 1
                if max_len < le+1 and dp[st][st+le] == 1:
                    max_len = le+1
                    start = st
                    end = st+le + 1
        return s[start:end]
