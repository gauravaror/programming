class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums)-1
        while start < end-1:
            mid = start + (end-start)//2
            if nums[mid] > nums[end]:
                start = start + 1
            elif nums[mid] < nums[end]:
                end = mid
            elif nums[mid-1] < nums[mid-1]:
                end = mid-1
        while end > 0 and nums[end-1] < nums[end]:
            end -= 1
        #print(start, end, mid)
        if target == nums[end]:
            return end
        elif target <= nums[len(nums)-1]:
            start = end
            end = len(nums) -1
        else:
            start = 0
            end = end-1
        print(start, end)
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid-1        
        return -1
