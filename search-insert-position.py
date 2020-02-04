class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = (start + end)//2
        while start < end:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid-1
            else:
                start =  mid + 1
            mid = (start + end)//2
        if nums[start] == target:
            return start
        elif nums[start] < target:
            return start + 1
        return start 
