class Solution:
    def rob1(self, nums: List[int]) -> int:
        prevprev = 0
        prev = 0
        for i in nums:
            prev,prevprev = max(prev, prevprev + i),prev
        return prev
        
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[1:]) , self.rob1(nums[:-1]))
