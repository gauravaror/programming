class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ah = []
        bh = []
        sol = []
        for i in A:
            heapq.heappush(ah, [i[1],i[0]])
        for j in B:
            heapq.heappush(bh, [j[1],j[0]])
        while len(ah) > 0 and len(bh) > 0:
            ta = heapq.heappop(ah)
            tb = heapq.heappop(bh)
            #print(ta, tb)
            if tb[0] > ta[0]:
                if tb[1] <= ta[0]:
                    sol.append([max(tb[1],ta[1]), ta[0]])
                heapq.heappush(bh, tb) 
            elif tb[0] == ta[0]:
                sol.append([max(tb[1],ta[1]),ta[0]])
            else:
                if ta[1] <= tb[0]:
                    sol.append([max(ta[1],tb[1]), tb[0]])
                heapq.heappush(ah, ta)
            #print(ah, bh)
        return sol
