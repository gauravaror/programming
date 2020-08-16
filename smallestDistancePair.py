class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        def feasible(sol):
            count, fast, slow = 0, 0, 0
            while slow < n or fast < n:
                if fast < n and nums[fast] - nums[slow] <= sol:
                    count += fast-slow
                    fast += 1
                else:
                    slow += 1
                if count >= k:
                    return True
            return False
        start = 0
        end = nums[-1] - nums[0]
        while start < end:
            mid = start + (end-start)//2
            if feasible(mid):
                end = mid
            else:
                start = mid + 1
        return start
