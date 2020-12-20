class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        self.dp = {}
        @lru_cache(None)
        def get_max(index):
            if index in self.dp:
                return self.dp[index]
            if index >= len(nums)-1:
                return 0
            maxa = -float('inf')
            for i in range(index+1, min(len(nums), index+ k+1)):
                maxa = max(maxa,  nums[i] + get_max(i))
            self.dp[index] = maxa
            return maxa
        ans = nums[0] + get_max(0)
        return ans
                
