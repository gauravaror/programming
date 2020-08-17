class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hh = {}
        for i in nums:
            if i in hh:
                return True
            else:
                hh[i] = True
        return False
