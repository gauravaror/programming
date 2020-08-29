import heapq
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = [(0, (0,0,0,0),0)]
        seen = {}
        tuptarget = [int(i) for i in target]
        def dist(us):
            d = 0
            for i,j in zip(us,tuptarget):
                d += abs(i-j)
            #print("Dist", us, tuptarget, d)
            return d
        neigh = []
        for i in range(4):
                crepr = tuptarget.copy()
                crepr[i] = tuptarget[i] + 1%10
                item = ''.join([str(i) for i in crepr])
                neigh.append(item in deadends)
                if tuptarget[i]  == 0:
                    crepr[i] = 9
                else:
                    crepr[i] = tuptarget[i] - 1%10
                item = ''.join([str(i) for i in crepr])
                neigh.append(item in deadends)
        if all(neigh):
            return -1
        while len(queue) > 0:
            _, repre, moves = heapq.heappop(queue)
            #if moves >= 0:
            #    print(repre, moves, queue)
            seen[repre] = True
            item = ''.join([str(i) for i in repre])
            if item in deadends:
                continue
            #print(item, target)
            if item == target:
                return moves
            for i in range(4):
                crepr = list(repre)
                crepr[i] = repre[i] + 1%10
                if not tuple(crepr) in seen:
                    heapq.heappush(queue, (dist(crepr), tuple(crepr), moves+1)) 
                if repre[i]  == 0:
                    crepr[i] = 9
                else:
                    crepr[i] = repre[i] - 1%10
                if not tuple(crepr) in seen:
                    heapq.heappush(queue, (dist(crepr), tuple(crepr), moves+1))        
        return -1
