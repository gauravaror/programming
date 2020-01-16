from collections import defaultdict
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        end = 0
        if len(nums) == 0:
            return 0
        current_sum = nums[start]
        min_size = float('inf')
        while(start < len(nums)):
            if (current_sum < s):
                if end < len(nums)-1:
                    end += 1
                    current_sum += nums[end]
                else:
                    break
            else:
                current_length = end - start + 1
                if current_length < min_size:
                    min_size = current_length
                current_sum -= nums[start]
                start += 1
        if min_size == float('inf'):
            return 0
        else:
            return min_size
