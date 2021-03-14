class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        dp = [[float('inf')]*len(nums) for _ in range(len(nums))]
        dp[k][k] = nums[k]
        ans = 0
        for r in range(len(nums)-k):
            for l in range(k+1):
                if k-l>=0 and k+r < len(nums):
                    a = r-1 if r > 0 else r
                    b = l-1 if l > 0 else l
                    dp[k + r][k - l] = min(dp[k + r][k - l],
                                           dp[k + a][k - b],
                                           nums[k-l], nums[k+r])
                    ans = max(ans, dp[k+ r][k - l]*(l+r+1))
        return ans
                
            
