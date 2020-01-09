# https://leetcode.com/problems/summary-ranges/submissions/
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        range_start = None
        if len(nums) == 0:
            return nums
        
        prev = nums[0]
        for i in nums[1:]:
            if prev + 1 == i:
                if range_start == None:
                    range_start = prev
            else:
                if range_start == None:
                    ranges.append(str(prev))
                else:
                    entry = str(range_start) + "->" + str(prev)
                    ranges.append(entry)
                range_start = None
            prev = i
        if range_start == None:
            ranges.append(str(prev))
        else:
            entry = str(range_start) + "->" + str(prev)
            ranges.append(str(entry))
        return ranges
        
