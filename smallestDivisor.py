import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        su = sum(nums)
        def divisor_thresh(div):
            if div == 0:
                return False
            ths = sum([math.ceil(i/div) for i in nums])
            return True if ths <= threshold else False
        start = 0
        end = su
        while start < end:
            mid = start + (end-start)//2
            if divisor_thresh(mid):
                end = mid
            else:
                start = mid + 1
        return start
