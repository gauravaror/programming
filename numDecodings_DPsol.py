class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            if s[i-1] != "0" and s[i] != "0" and int(s[i-1:i+1]) <= 26:
                dp[i+1] = dp[i-1] + dp[i]
            elif s[i-1] != "0" and s[i] != "0":
                dp[i+1] = dp[i]
            elif s[i-1] == '0' and s[i] != '0':
                dp[i+1] = dp[i]
            elif s[i] == '0' and s[i-1] != '0' and int(s[i-1]) <= 2:
                dp[i+1] = dp[i-1]
            else:
                dp[i+1] = 0
        return dp[len(s)]
