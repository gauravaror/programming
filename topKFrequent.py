from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elems = Counter()
        for i in nums:
            elems[i] += 1
        hp = []
        for t,v in elems.items():
            heapq.heappush(hp, (v,t))
            #print(t, v, hp)
            while len(hp) > k:
                #print(hp, len(hp), t)
                heapq.heappop(hp)
        #print(hp)
        return [i[1] for i in hp]
