class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [-1]*len(nums)
        dp[len(nums)-1] = 0
        for i in range(len(nums)-1)[::-1]:
            allowed_steps = nums[i]
            for pos in range(i+1, i+allowed_steps+1):
                #print(i, pos)
                if pos < len(nums):
                    if dp[pos] != -1:
                        dp[i] = pos - i + dp[pos]
                        break
                    if dp[pos] == -1 and nums[i] - (pos-i) <= nums[pos]:
                        break
                        
        #print(dp)
        if dp[0] != -1:
            return True
        else:
            return False
