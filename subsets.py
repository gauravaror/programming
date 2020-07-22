class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        n = len(nums)
        for i in range(n):
            output.extend([curr + [nums[i]] for curr in output])
        return output
