from heapq import heappush, heappop
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for a,b in classes:
            h = b-a
            h = h/(b*(b+1))
            if h != 0:
                heappush(heap, (1/h, a,b, a/b))
            else:
                heappush(heap, (float('inf'), a,b, a/b))
        while extraStudents:
            _, a,b, _ = heappop(heap)
            a += 1
            b += 1
            h = b-a
            h = h/(b*(b+1))
            if h != 0:
                heappush(heap, (1/h, a, b, a/b))
            else:
                heappush(heap, (float('inf'), a, b, a/b))
            extraStudents -= 1
        return sum([ i[3] for i in heap])/len(classes)
