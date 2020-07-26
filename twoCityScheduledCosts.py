from heapq import *
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        mhe = []
        total = len(costs)//2
        output = 0
        numA = 0
        numB = 0
        for idx,i in enumerate(costs):
            cst = 1/abs(i[0]-i[1]) if i[0] != i[1] else 100
            heappush(mhe, (cst, idx))
        while len(mhe) > 0:
            elem = heappop(mhe)
            ccost = costs[elem[1]]
            diff = ccost[0] - ccost[1]
            if diff > 0:
                if numB < total:
                    output +=  ccost[1]
                    numB += 1
                else:
                    output += ccost[0]
                    numA += 1
            else:
                if numA < total:
                    output += ccost[0]
                    numA += 1
                else:
                    output += ccost[1]
                    numB += 1
        return output
