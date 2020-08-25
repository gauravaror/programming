class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')]*366
        dp[0] = 0
        for i in range(1, 366):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                print(i, min(dp[max(0, i-1):i+1]) + costs[0], 
                         min(dp[max(0,i-7):i+1]) + costs[1],
                        min(dp[max(0,i-30):i+1]) + costs[2])
                        
                dp[i] = min(dp[i], min(dp[max(0, i-1):i+1]) + costs[0],
                            min(dp[max(0,i-7):i+1]) + costs[1],
                            min(dp[max(0,i-30):i+1]) + costs[2])
        print(dp)
        return dp[days[-1]]
