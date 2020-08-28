class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        end = 0
        greater = []
        longest_size = 0
        while end < len(nums):
            if len(greater) == 0:
                longest_size = max(longest_size, end-start)
                for j in range(start, end):
                    diff = abs(nums[j] -nums[end])
                    if  diff > limit:
                        greater.append(diff)
                end += 1
            else:
                remove = nums[start]
                start += 1
                for i in range(start, end):
                    diff = abs(remove - nums[i] )
                    if diff > limit:
                        greater.remove(diff)
        if len(greater) == 0:
                longest_size = max(longest_size, end-start)
        return longest_size
