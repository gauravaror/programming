from collections import Counter
from heapq import heappush, heappop
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half_elems = len(arr) // 2
        counter = Counter()
        for i in arr:
            counter[i] += 1
        elems = 0
        elem_sum = 0
        for i,j in counter.most_common():
            elem_sum += j
            elems += 1
            if elem_sum >= half_elems:
                break
        return elems
