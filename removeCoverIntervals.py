class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        start, end = intervals[0]
        removed = 0
        for i in range(1, len(intervals)):
            cint = intervals[i]
            if (cint[0] >= start and cint[1] <= end):
                removed += 1
            elif (cint[0] <= start and cint[1] >= end):
                removed += 1
                start, end = cint
            else:
                start, end = cint
        return len(intervals) - removed 
