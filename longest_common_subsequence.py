class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*len(text2) for _ in range(len(text1))]
        for in1 in range(len(text1)):
            for in2 in range(len(text2)):
                if text1[in1] == text2[in2]:
                    temp = 1
                    if in1>0 and in2>0:
                        temp += dp[in1-1][in2-1]
                    dp[in1][in2] = max(temp, dp[in1][in2])
                elif in1 > 0 and in2 > 0:
                    dp[in1][in2] += max(dp[in1][in2], dp[in1-1][in2-1], dp[in1-1][in2], dp[in1][in2-1])
                else:
                    allowed_in1 = in1
                    allowed_in2 = in2
                    if allowed_in1 > 0:
                        allowed_in1 -= 1
                    if allowed_in2 > 0:
                        allowed_in2 -= 1
                    dp[in1][in2] = dp[allowed_in1][allowed_in2]
        #print(dp)
        return dp[len(text1)-1][len(text2)-1]
