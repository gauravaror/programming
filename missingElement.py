class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        starting = nums[0]
        start = 0
        end = len(nums)
        while start < end:
            mid = start + (end-start)//2
            if nums[mid]- starting - mid >= k:
                end = mid
            else:
                start = mid + 1
        start = start-1
        print(start)
        return nums[start] +  (k- (nums[start] -starting-start))
