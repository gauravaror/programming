class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hh = {}
        for i in nums:
            if i in hh:
                del hh[i]
            else:
                hh[i] = True
        return hh.keys()
