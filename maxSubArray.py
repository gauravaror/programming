class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum = 0
        ma = -float('inf')
        for n in nums:
            cum = n + (cum if cum >0 else 0)
            ma = max(ma, cum)
        return ma
