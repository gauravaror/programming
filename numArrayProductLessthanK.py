class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        current_product = 1
        ans = 0
        while end < len(nums) and start < len(nums):
            if current_product < k and end < len(nums):
                current_product *= nums[end]
                end += 1
            else:
                current_product /= nums[start]
                start += 1
                if end < start:
                    end = start
                    current_product = 1
            #print(ans, start, end, end-start, current_product)
            if current_product < k:
                ans += (end-start)
        if current_product > k:
            while current_product >= k and start < len(nums):
                current_product /= nums[start]
                start += 1
            ans += end-start
        return ans
