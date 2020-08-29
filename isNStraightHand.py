import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        pqueue = []
        c = Counter()
        c.update(hand)
        for key,val in c.items():
            heapq.heappush(pqueue, (key,val))
        resting = []
        prev = None
        curr_len = 0
        while len(pqueue) > 0:
            #print(pqueue)
            key,val = heapq.heappop(pqueue)
            if prev:
                if prev + 1 != key:
                    return False
            curr_len += 1
            prev = key
            val -= 1
            if val > 0:
                resting.append((key, val))
            if curr_len == W:
                curr_len = 0
                prev = None
                for i in resting:
                    heapq.heappush(pqueue, i)
                resting = []
        #print(pqueue, resting, curr_len)
        if len(pqueue) != 0 or len(resting) != 0 or curr_len != 0:
            return False
        else:
            return True
