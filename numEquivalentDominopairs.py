from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hh = defaultdict(lambda: 0)
        for i in dominoes:
            if i[0] < i[1]:
                a = (i[0],i[1])
            else:
                a = (i[1], i[0])
            hh[a] += 1
        pairs = 0
        for i,j in hh.items():
            if j > 1:
                pairs += j*(j-1)//2
        return pairs
