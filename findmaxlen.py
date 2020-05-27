class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        hh = {0: -1}
        cum = 0
        maxlen = 0
        for i in range(len(nums)):
            cum += nums[i]
            d = 2*cum - (i+1)
            if d not in hh:
                hh[d] = i
            else:
                maxlen = max(maxlen, i - hh[d])
        return maxlen
