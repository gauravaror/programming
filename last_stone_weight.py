class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            nw = abs(stones[-1] - stones[-2])
            del stones[-1]
            del stones[-1]
            if nw > 0:
                stones.append(nw)
            print(stones)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
