class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hh = {}
        for i in nums:
            if i in hh:
                del hh[i]
            else:
                hh[i] = 1
        return list(hh.keys())[0]
