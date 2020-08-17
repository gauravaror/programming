class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        prev = nums[0]
        pprev = 0
        for i in nums[1:]:
            tmp = max(prev, pprev+i)
            pprev = prev
            prev = tmp
        return prev
