class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x : x[0])
        output = []
        start, end = intervals[0]
        print(intervals)
        for interval in intervals[1:]:
            if interval[0] > end:
                output.append([start, end])
                start, end = interval
            else:
                if interval[1] > end:
                    end = interval[1]
                if interval[0] < start:
                    start = interval[0]
        output.append([start, end])
        return output
