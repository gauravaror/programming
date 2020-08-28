class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        cumsum = 0
        dp = {0:-1}
        best_till = {-1: float('inf')}
        best = float('inf')
        ans = float('inf')
        for i in range(len(arr)):
            cumsum += arr[i]
            if cumsum-target in dp:
                end = dp[cumsum-target]
                ans = min(ans, i-end + best_till[end])
                best = min(best, i-end)
            dp[cumsum] = i
            best_till[i] = best
        #print(best_till, dp)
        return -1 if ans == float('inf') else ans
