class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        start = 1
        end = max(bloomDay) + 1
        maxbloom = max(bloomDay)
        def feasible(day):
            consdays = 0
            groups = 0
            for i in bloomDay:
                if day >= i:
                    consdays += 1
                else:
                    consdays = 0
                if consdays == k:
                    consdays = 0
                    groups += 1
                #print(i, groups, consdays)
            print(day, groups, consdays)
            if groups < m:
                return False
            else:
                return True
        while start < end:
            mid = start + (end-start)//2
            print(start, end, mid, feasible(mid))
            if feasible(mid):
                end = mid
            else:
                start = mid + 1
        if start <= maxbloom:
            return start
        else:
            return -1
