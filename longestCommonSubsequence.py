class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*len(text2) for _ in range(len(text1))]
        dp[0][0] = int(text2[0] == text1[0])
        for i in range(1, len(text2)):
            dp[0][i] = max(dp[0][i-1], int(text2[i] == text1[0]))
        for j in range(1, len(text1)):
            dp[j][0] = max(dp[j-1][0], int(text1[j] == text2[0]))
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return max([ max(i) for i in dp])
