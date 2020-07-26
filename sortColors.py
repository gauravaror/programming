from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter()
        for i in nums:
            c[i] += 1
        idx = 0
        for i in [0,1,2]:
            for j in range(c[i]):
                nums[idx] = i
                idx += 1
