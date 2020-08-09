from collections import defaultdict
from heapq import *
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dic = defaultdict(list)
        dic[0].append(-1)
        cum = 0
        pos = []
        last_done = -1
        for i  in range(len(nums)):
            cum += nums[i]
            dic[cum].append(i)
            if cum-target in dic:
                for it in dic[cum-target]:
                    if it+1 <= i and it+1 > last_done:
                        pos.append((i, it+1, i))
                        last_done = i
        return len(pos)
