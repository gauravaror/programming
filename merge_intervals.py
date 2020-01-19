class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key= lambda x: x[0])
        if len(intervals) == 0:
            return intervals
        current = intervals[0]
        new_intervals = []
        for i in intervals[1:]:
            if current[1] >= i[0]:
                current[1] = max(i[1], current[1])
            else:
                new_intervals.append(current)
                current = i
        new_intervals.append(current)
        return new_intervals
