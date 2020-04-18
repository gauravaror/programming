class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dp = [[0]*len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[0][i] = nums[i]
        max_continous = 0
        for leng in range(1, len(nums)):
            for point in range(leng, len(nums)):
                dp[leng][point] = dp[leng-1][point-1] + nums[point]
                if (leng+1)/2 == dp[leng][point]:
                    max_continous = leng+1
        #print(dp)
        return max_continous
