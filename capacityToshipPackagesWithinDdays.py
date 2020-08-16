class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        total_weight = sum(weights)
        start = 0
        end = total_weight
        def shipped(thisweight):
            print("shipped", thisweight)
            required = 1
            curr = 0
            for i in weights:
                if i > thisweight:
                    return False
                if curr + i > thisweight:
                    required += 1
                    curr = i
                else:
                    curr += i
            print("required", thisweight, required, D)
            if required <= D:
                return True
            else:
                return False

        while start < end:
            mid = start + (end-start)//2
            if shipped(mid):
                end = mid
            else:
                start = mid+1
        print(start, end, mid)
        return start
