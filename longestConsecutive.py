class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hh = {}
        if len(nums) == 0:
            return 0
        
        for n in nums:
            if n-1 in hh:
                hh[n] = hh[n-1] + 1
                n += 1
                while n in hh:
                    hh[n] = hh[n-1] + 1
                    n += 1
            else:
                hh[n] = 1
                n += 1
                while n in hh:
                    hh[n] = hh[n-1] + 1
                    n += 1
        print(hh)
        return max(hh.values())
