class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        for idx,i in enumerate(intervals):
            starts.append((i[0], idx))
        starts = sorted(starts)
        def bs(target):
            start = 0
            end = len(starts)-1
            while start < end:
                mid = start + (end-start)//2
                if starts[mid][0] >=  target:
                    end = mid
                else:
                    start = mid + 1
            print(starts[start], target, start)
            if starts[start][0] < target:
                return -1
            else:
                return starts[start][1]
        output = []
        for i in intervals:
            output.append(bs(i[1]))
        return output
