class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_seq = 1
        if len(nums) == 0:
            return 0
        current_num = nums[0]
        current_seq = 1
        for i in nums[1:]:
            if i > current_num:
                current_seq += 1
            else:
                current_seq = 1
            if (current_seq > longest_seq):
                longest_seq = current_seq
            current_num = i
        return longest_seq
            
            
        
