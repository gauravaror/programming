class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones.sort()
        print(stones)
        while (len(stones)>1):
            first_stone = stones[0]
            second_stone = stones[1]
            resulting = abs(first_stone - second_stone)
            stones.pop(0)
            stones.pop(0)
            if not resulting == 0:
                stones.insert(0, resulting)
            print(stones)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
