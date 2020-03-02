class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums = [(i, idx) for idx,i in enumerate(nums)]
        new_nums.sort()
        prev = None
        prev_idx = None
        for idx,i in enumerate(new_nums):
            #print(i, prev, i[0], i[1], prev_idx, prev is i[0])
            if (not prev is None) and (prev is i[0]):
                nums[i[1]] = prev_idx
            else:
                nums[i[1]] =  idx
                prev = i[0]
                prev_idx = idx
            #print(nums)
        return nums
