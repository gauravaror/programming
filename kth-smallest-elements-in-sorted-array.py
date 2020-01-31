class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ho = []
        for i in matrix:
            heapq.heappush(ho, (i[0], i))
        index = 1
        while (index <= k):
            #print(ho)
            elem = heapq.heappop(ho)
            if (index  == k):
                return elem[0]
            if len(elem[1]) > 1:
                elem = elem[1][1:]
                #print(elem)
                heapq.heappush(ho, (elem[0], elem))
            index += 1
        return -1
