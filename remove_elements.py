class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        itr = 0
        deleted = False
        while(itr < len(nums)):
            if (nums[itr] == val):
                nums.remove(val)
            else:
                itr += 1
        return len(nums)
