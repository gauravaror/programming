class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
            #print(i, dp)
        maxa = max(dp[:])
        #print(nums, dp)
        if maxa == 0:
            return 1
        else:
            return maxa
