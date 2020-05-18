class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end  = len(nums)-1
        while start < end:
            mid = (start + end) //2
            print(start, end, mid)
            if nums[mid] > nums[start]  and nums[mid] > nums[end]:
                start1 = mid - (mid-start)//2
                end1 = mid + (end - mid)//2
                if nums[start1] > nums[mid]:
                    end = mid-1
                elif nums[end1] > nums[mid]:
                    start = mid + 1
                else:
                    start -= 1
                    end -= 1
            elif nums[mid] < nums[start] and nums[mid] < nums[end]:
                if nums[start] > nums[end]:
                    end = mid-1
                else:
                    start = mid + 1
            elif nums[start] >= nums[mid] and nums[mid] >= nums[end]:
                end = mid-1
            elif nums[start] <= nums[mid] and nums[mid] <= nums[end]:
                start = mid+1
        return start
