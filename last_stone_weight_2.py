class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        knapsack_w =  (total_sum//2)
        #print(total_sum, knapsack_w)
        dp = [False]*(knapsack_w + 1)
        dp[0] = True
        for j in stones:
            position = []
            for i in range(knapsack_w+1):
                if i+j < knapsack_w+1:
                    if dp[i]:
                        #print(i,j, i+j)
                        position.append(i+j)
            for p in position:
                dp[p] = True
        #print(dp)
        for d in range(1, knapsack_w+1)[::-1]:
            if dp[d]:
                return total_sum - d - d
