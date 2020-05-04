class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = [1]*len(nums)
        ms = 0
        for f in range(1,len(nums)):
            for l in range(f):
                if nums[f] > nums[l]:
                    dp[f] = dp[l] + 1
                if dp[f] > ms:
                    ms = dp[f]
        print(dp)
        if ms >= 3:
            return True
        else:
            return False
