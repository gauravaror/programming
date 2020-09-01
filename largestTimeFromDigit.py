class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        maxtime = -float('inf')
        retrn = ""
        def back(current, nums):
            nonlocal maxtime
            nonlocal retrn
            if len(nums) == 0:
                hours = current[0]*10 + current[1]
                minutes = current[2]*10 + current[3]
                if hours > 23 or minutes > 59:
                    return
                if maxtime < hours*60 + minutes:
                    maxtime = hours*60 + minutes
                    retrn = str(hours).zfill(2) + ':' + str(minutes).zfill(2)
            for i in range(len(nums)):
                back(current + [nums[i]], nums[:i] + nums[i+1:])
        back([], A)
        return retrn
