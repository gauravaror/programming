from heapq import *
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        front_heap = []
        num_heap = []
        output = []
        for i  in people:
            if i[1] == 0:
                heappush(num_heap, i)
            else:
                front_heap.append((i, i[1]))
        
        while len(num_heap) > 0:
            elem = heappop(num_heap)
            output.append(elem)
            for idx in range(len(front_heap)):
                tel = front_heap[idx]
                if not tel:
                    continue
                if elem[0] >= tel[0][0]:
                    ne = tel[1] - 1
                    if ne == 0:
                        front_heap[idx] = None
                        heappush(num_heap, tel[0])
                    else:
                        front_heap[idx] = (tel[0], ne)
        return output
