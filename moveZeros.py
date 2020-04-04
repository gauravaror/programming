class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        len_ =  len(nums)
        removed_zeros = 0
        while i < len_:
            if nums[i] ==  0:
                del nums[i]
                len_ = len(nums)
                removed_zeros += 1
            else:
                i += 1
        while removed_zeros > 0:
            nums.append(0)
            removed_zeros -= 1
