class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.robber(nums[:-1]), self.robber(nums[1:]))
    
    def robber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        pprev = 0
        prev = nums[0]
        for i in nums[1:]:
            tmp = max(prev, pprev+i)
            pprev = prev
            prev = tmp
        print(nums, prev)
        return prev
