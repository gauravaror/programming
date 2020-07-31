class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        output = 0
        for i in range(len(s)):
            dp[i][i] = 1
            output += 1
        for le in range(1, len(s)):
            for i in range(len(s)-le):
                #print(i, le)
                mid = (le + 1)//2
                fstart = i
                fend = i + mid 
                sstart = i+ mid
                send = i+ le + 1
                if (le + 1) % 2 != 0:
                    sstart += 1
                #print("dfsd",fstart, fend, sstart, send, s[fstart:fend], s[sstart:send][::-1])
                #  dp[fstart][fend-1] == 1 and dp[sstart][send-1] == 1 and 
                if s[fstart:fend] == s[sstart:send][::-1]:
                    dp[i][i+le] = 1
                    output += 1
        #print(dp)
        return output
