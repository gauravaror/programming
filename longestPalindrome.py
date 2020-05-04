class Solution:
    def longestPalindrome(self, s: str) -> str:
        first = s
        second = s[::-1]
        dp = [[0]*len(s) for _ in range(len(s))]
        max_str = None
        max_len = 0
        for f in range(len(first)):
            for sd in range(len(second)):
                s_ind = sd
                f_ind = f
                if sd == 0 or f ==0 :
                    s_ind = sd
                    f_ind = f
                else:
                    s_ind -= 1
                    f_ind -= 1
                if first[f] == second[sd]:
                    dp[f][sd] = dp[f_ind][s_ind] + 1
                if dp[f][sd] > max_len:
                    ns = s[f-(dp[f][sd]-1):f+1]
                    if ns == ns[::-1]:
                        max_len = dp[f][sd]
                        max_str = ns

        if not max_str:
            return ""
        return max_str
