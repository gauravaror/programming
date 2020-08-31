class Solution:
    def solve(self, house, color):
        if (house, color) in self.dp:
            return self.dp[house,color]
        if house >= self.maxhouse:
            return 0
        mincost = float('inf')
        for i in [0,1,2]:
            if i != color:
                mincost = min(mincost, self.costs[house][i] + self.solve(house+1, i))
        self.dp[house,color] = mincost
        return mincost
                
        
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0 
        self.costs = costs
        self.dp = {}
        self.maxhouse = len(costs)
        return min(self.costs[0][0] + self.solve(1, 0), self.costs[0][1] + self.solve(1,1), self.costs[0][2] +  self.solve(1,2))
