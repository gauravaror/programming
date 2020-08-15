class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp_left = [1]*len(nums)
        dp_right = [1]*len(nums)
        cum = 1
        len_nums = len(nums)
        for i  in range(len_nums):
            cum*= nums[i]
            dp_left[i] = cum
        cum = 1
        for j in range(len_nums)[::-1]:
            cum *= nums[j]
            dp_right[j] = cum
        nums[0] = dp_right[1]
        nums[len_nums-1] = dp_left[len_nums-2]
        for i in range(1, len_nums-1):
            nums[i] = dp_left[i-1]*dp_right[i+1]
        return nums  
        
