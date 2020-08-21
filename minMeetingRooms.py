class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        if len(intervals) == 0:
            return 0
        time, end = intervals[0]
        activemeetings = [end]
        needed_rooms = 1
        for i in intervals[1:]:
            time = i[0]
            for g in activemeetings:
                if g <= time:
                    activemeetings.remove(g)
    
            if i[0] < end:
                activemeetings.append(i[1])
                if len(activemeetings) > needed_rooms:
                    needed_rooms = len(activemeetings)
            else:
                activemeetings.append(i[1])
            end = i[1]
        return needed_rooms
