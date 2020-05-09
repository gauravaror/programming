class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        maxlen = 1
        end = 0
        dp = {s[0] : True}
        for i in range(1, len(s)):
            mid = i//2
            #print(dp, i, s[mid:i+1], s[mid+1:i+1], maxlen )
            if i % 2 == 0:
                if s[mid:i+1] in dp:
                    maxlen = i +1
                    end  = i
            else:
                if s[mid+1:i+1] in dp:
                    maxlen = i+1
                    end = i
            if i < len(s)//2 + 1:
                dp[s[:i+1][::-1]] = True
        #print(maxlen)
        return s[maxlen:][::-1] + s
