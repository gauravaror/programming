class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_ = nums[0]
        prev = nums[0]
        current = nums[0]
        for i in nums[1:]:
            if prev < i:
                current += i
                prev = i
            else:
                current = i
                prev = i
            max_ = max(max_, current)
        return max_
                
        
