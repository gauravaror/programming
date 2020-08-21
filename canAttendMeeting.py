class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        intervals = sorted(intervals)
        end  = intervals[0][1]
        for i in intervals[1:]:
            if i[0] < end:
                return False
            else:
                end = i[1]  
        return True
