class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sorted(intervals, key=lambda x: x[1])
        start, end = newInterval
        in_added = False
        output = []
        for i in intervals:
            if i[1] <  start:
                output.append(i)
            elif i[0] > end:
                if not in_added:
                    output.append([start, end])
                    in_added = True
                output.append(i)
            else:
                start = min(start, i[0])
                end = max(end, i[1])
        if not in_added:
            output.append([start, end])
        return output
