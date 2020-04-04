class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[cur] == 0:
                nums[cur] = nums[i]
                nums[i] = 0
            while cur < i and nums[cur] != 0:
                cur +=1
