class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hh = {}
        for idx,n in enumerate(nums):
            hh[n] = idx
        pairs  = []
        for idx,n in enumerate(nums):
            if target-n in hh:
                if hh[target-n] > idx:
                    pairs.append([idx, hh[target-n]])
                
        return pairs[0]
