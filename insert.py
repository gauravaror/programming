class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        in_started = False
        added = False
        in_start, in_end = newInterval
        for i  in intervals:
            start, end = i
            if in_start > end:
                output.append(i)
            elif not added and not in_started and  in_end < start:
                output.append(newInterval)
                added = True
                output.append(i)
            elif start <= in_start and end >= in_end:
                return intervals
            elif not added and start > in_end:
                output.append([in_start, in_end])
                added = True
                output.append(i)
                in_started = False
            elif in_end < start:
                output.append(i)
            elif start >= in_start and in_start < end and end >= in_end:
                in_started = True
                in_end =  end
            elif end <= in_end:
                in_start = min(start, in_start)
                in_started = True
            elif in_started:
                in_start = min(start, in_start)
                in_end = max(end, in_end)
        if not added:
            output.append([in_start, in_end])
        return output 
