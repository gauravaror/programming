class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        start = 0
        end = len(nums) - 1
        def find_end(mid):
            smid = mid
            emid = mid
            while smid >= 0 and nums[smid] == target:
                smid -=1
                
            while emid < len(nums) and nums[emid] == target:
                emid += 1
            return [smid +1, emid-1]
                
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return find_end(mid)
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return [-1,-1]
