class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        start = 0
        end = sum(sweetness)//(K+1) + 1
        def feasible(min_sweet):
            nonlocal sweetness
            curr = 0
            steps = 0
            for i in sweetness:
                curr += i
                if curr >= min_sweet:
                    steps += 1
                    curr = 0
            if steps < K+1:
                return True
            else:
                return False
            
        while start < end:
            mid = start + (end-start)//2
            if feasible(mid):
                end = mid
            else:
                start = mid + 1
        return start - 1
