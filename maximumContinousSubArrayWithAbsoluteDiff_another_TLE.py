class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        end = 0
        longest_size = 0
        maxa = nums[0]
        mina = nums[0]
        while end < len(nums):
            if maxa - mina <= limit:
                longest_size = max(longest_size, end-start)
                maxa = max(maxa, nums[end])
                mina = min(mina, nums[end])
                end += 1
            else:
                remove = nums[start]
                start += 1
                if remove == mina:
                    mina = min(nums[start:(end+1)])
                if remove == maxa:
                    maxa = max(nums[start:(end+1)])
        if maxa-mina <= limit:
                longest_size = max(longest_size, end-start)
        return longest_size
