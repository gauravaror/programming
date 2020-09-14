class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prevprev = 0
        prev = nums[0]
        for i in nums[1:]:
            curr = max(prev, prevprev+i)
            prevprev = prev
            prev = curr
        return prev
