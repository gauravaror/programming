class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        start = 1
        end = m*n
        def feasible(num):
            ad  = 0
            for i in range(1, m+1):
                add = min(num//i, n)
                ad += add
                if ad >= k:
                    return True
            return False if ad < k else True
        while start < end:
            mid = start + (end-start)//2
            if feasible(mid):
                end = mid
            else:
                start = mid + 1
        return start
