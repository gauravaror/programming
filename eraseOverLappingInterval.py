from heapq import *
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        hh = []
        for i in intervals:
            heappush(hh, (i[1], i))
        output = []
        while len(hh) > 0:
            le,el = heappop(hh)
            add = True
            for i in output:
                if el[0] < i[1] and el[0] >= i[0]:
                    add = False
                if el[1] <= i[1] and el[1] >= i[0]:
                    add = False
                if i[0] >= el[0] and i[1] <= el[1]:
                    add = False
            if add:
                output.append(el)
        #print(output)  
        return len(intervals) - len(output)
