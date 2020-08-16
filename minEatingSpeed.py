import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        start = 0
        end = max(piles)
        def feasible(K):
            h_needed = 0
            if K == 0:
                return False
            for i in piles:
                h_needed += math.ceil(i/K)
#                h_needed += 1
                if h_needed > H:
                    return False
            return True
        while start < end:
            mid = start + (end-start)//2
            print(start, end , mid)
            if feasible(mid):
                end = mid
            else:
                start = mid + 1
        return start
