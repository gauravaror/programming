from collections import Counter
from heapq import *
class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter()
        c.update(S)
        iheap = []
        wheap = []
        for k,v in c.items():
            heappush(iheap, (1/v, k, v))
        output = ""
        time = 0
        print(iheap)
        while len(iheap) + len(wheap) > 0:
            print(iheap)
            if len(iheap) == 0:
                return ""
            _,k,v = heappop(iheap)
            output += k
            while len(wheap) > 0:
                _, k1, v1 = heappop(wheap)
                heappush(iheap, (1/v1,k1,v1))
            v -= 1
            if v != 0:
                heappush(wheap, (time, k, v))            
            time += 1
        return output
