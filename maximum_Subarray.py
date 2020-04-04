class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0 
        end = 0
        max_sum = -float('inf')
        maxi = 0
        min_sum = float('inf')
        mini = 0
        max_num = -float('inf')
        current_sum = 0
        for idx,a in enumerate(nums):
            current_sum += a
            if current_sum > max_sum:
                max_sum = current_sum
                maxi = idx
            if current_sum < min_sum:
                min_sum = current_sum
                mini = idx
            if a > max_num:
                max_num = a
            if current_sum < 0:
                current_sum = 0
                min_sum = 0
        if max_sum < 0:
            return max_num
        else:
            il = max_sum - min_sum
            if mini > maxi:
                il = max_sum
            return max(il, max_sum, min_sum)

