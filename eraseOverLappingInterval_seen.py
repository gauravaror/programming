class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        #print(intervals)
        end_time = -float('inf')
        skip = 0
        for i in intervals:
            #print(i, end_time)
            if i[0] < end_time:
                skip += 1
            else:
                end_time = i[1]
        return skip
