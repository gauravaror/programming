from collections import defaultdict
from heapq import *
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dic = defaultdict(list)
        dic[0].append(-1)
        cum = 0
        pos = []
        for i  in range(len(nums)):
            cum += nums[i]
            dic[cum].append(i)
            if cum-target in dic:
                for it in dic[cum-target]:
                    if it+1 <= i:
                        heappush(pos, (abs(i-it), it+1, i))
        output = []
        print(pos)
        while len(pos) > 0:
            _,start, end = heappop(pos)
            add = True
            for item in output:
                if (start <= item[1]) and (end >= item[0]):
                    add = False
            print(start, end , add)
            if add:
                output.append((start, end))
        return len(output)
        
