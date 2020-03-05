class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        maxi = sum(nums)
        if S > maxi:
            return 0
        total_range = 2*maxi + 1
        dp = [[0]*total_range for _ in range(len(nums))]
        dp[0][maxi + nums[0]] = 1
        dp[0][maxi - nums[0]] += 1

        for j,num in enumerate(nums[1:]):
            for i in range(total_range):
                num_ways = 0
                if num + i < total_range:
                    num_ways += dp[j][i+num]
                if i- num >= 0:
                    num_ways += dp[j][i-num]
                dp[j+1][i] = num_ways
        return dp[len(nums)-1][maxi+S]
