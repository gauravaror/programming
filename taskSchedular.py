from collections import Counter
from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter()
        c.update(tasks)
        hh = []
        th = []
        for k,v in c.items():
            heappush(hh, (1/v, (k,v)))
        time = 0
        while len(hh) + len(th) > 0:
            #print(hh, th)
            time += 1
            if len(hh) > 0:
                item = heappop(hh)
                k, v = item[1]
                if v-1 > 0:
                    heappush(th, (time, (k,v-1)))
            while len(th) > 0:
                titem = heappop(th)
                ttime, item1 = titem
                if time - ttime >= n:
                    heappush(hh, (1/item1[1], item1))
                else:
                    heappush(th, titem)
                    break
        return time
