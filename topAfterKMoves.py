class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if k %2 == 0:
                return nums[0]
            else:
                return -1
        if k == 0:
            return nums[0]
        if k-1 < len(nums):
            a = nums[:k-1]
            if len(a) == 0:
                maxa = -1
            else:
                maxa = max(a)
            if len(nums) > k:
                return max(maxa, nums[k])
            else:
                return maxa
        else:
            return max(nums)
