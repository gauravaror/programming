from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        no_trust = 1
        hh = defaultdict(list)
        tru = defaultdict(list)
        for i in trust:
            hh[i[0]].append(i[1])
            tru[i[1]].append(i[0])
            if i[0] == no_trust:
                no_trust = None
            if len(hh[i[1]]) == 0:
                no_trust = i[1]
        if no_trust and (len(tru[no_trust]) == N-1):
            return no_trust
        else:
            return -1
