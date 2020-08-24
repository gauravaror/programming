class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 1
        end  = 1
        while end < len(nums):
            if nums[end] == nums[end-1]:
                end += 1
            else:
                nums[start] = nums[end]
                start += 1
                end += 1
        while start < len(nums):
            del nums[start]
