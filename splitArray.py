class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start = 0
        end = sum(nums)
        def feasible(thisum):
            print(thisum)
            required = 1
            curr = 0
            for i in nums:
                if i > thisum:
                    return False
                elif curr + i > thisum:
                    required += 1
                    curr = i
                else:
                    curr += i
            if required <= m:
                return True
            else:
                return False

        while start < end:
            mid = start + (end-start)//2
            print(start, end, mid)
            if feasible(mid):
                end = mid
            else:
                start = mid + 1
        return start
