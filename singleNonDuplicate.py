class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start + end)//2
            print(start, end, mid)
            if mid == 0 or mid == len(nums)-1 :
                    break
            if nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
            else:
                if mid % 2 == 0:
                    if nums[mid] != nums[mid+1]:
                        end = mid
                    else:
                        start = mid+2
                else:
                    if nums[mid] != nums[mid-1]:
                        end = mid-1
                    else:
                        start = mid + 1
            print("dsd",start, end, mid)
                    
        
        if start == 0:
            return nums[start] if nums[start] != nums[start+1] else -1
        elif start == len(nums)-1:
            return nums[start] if nums[start] != nums[start-1] else -1
        else:
            return nums[start] if nums[start-1] != nums[start] and nums[start+1] != nums[start] else -1
