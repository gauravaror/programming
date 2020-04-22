class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = [[-1]*len(nums) for _ in range(len(nums))]
        obs = 0
        for i in range(len(nums)):
            dp[0][i] = nums[i]
            if dp[0][i] == k:
                obs += 1
        for le in range(1, len(nums)):
            for st in range(le, len(nums)):
                dp[le][st] = dp[le-1][st-1] + nums[st]
                if dp[le][st] == k:
                    obs += 1
        return obs
