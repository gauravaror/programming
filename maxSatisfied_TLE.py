class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        dp = [[0]*(X+2) for _ in range(len(customers))]
        for c in range(len(customers)):
            for d in range(X+2):
                if d == 0:
                    dp[c][0] = dp[c-1][0]
                    if grumpy[c] == 0:
                        dp[c][0] += customers[c]
                elif d in list(range(1, X+1)):
                    if c-d + 1 >= 0:
                        if c-1 >= 0:
                            dp[c][d] = dp[c-1][d-1]
                        dp[c][d] += customers[c]
                else:
                    if c-1 >= 0:
                        newval = dp[c-1][d-1]
                        newval1 = dp[c-1][d]
                    else:
                        newval = 0
                        newval1 = 0
                    if grumpy[c] == 0:
                        newval += customers[c]
                        newval1 += customers[c]
                    dp[c][d] = max(newval, newval1, dp[c][d-1])
        #print(dp)
        return dp[len(customers)-1][-1]
