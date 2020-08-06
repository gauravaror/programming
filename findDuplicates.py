class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        le = len(nums)
        for i in range(le):
            curr = nums[i]-1 if nums[i] <= le else nums[i]-le-1
            if nums[curr] > le:
                output.append(curr + 1)
            else:
                nums[curr] += le
        return output
