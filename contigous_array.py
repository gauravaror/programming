class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))
        cumulative = 0
        hh = {0:-1}
        max_len = 0
        for i in range(len(nums)):
            cumulative += nums[i]
            dp[i] = 2*cumulative - (i+1)
            if dp[i] not in hh:
                hh[dp[i]] = i
            else:
                this_len = i- hh[dp[i]]
                max_len = max(this_len, max_len)
        return max_len
