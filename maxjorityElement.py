from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_elem = 0
        max_count = 0
        hh = defaultdict(lambda: 0)
        for i in nums:
            hh[i] += 1
            if hh[i] > max_count:
                max_count = hh[i]
                max_elem = i
        if max_count >= len(nums)//2:
            return max_elem
        else:
            return -1
