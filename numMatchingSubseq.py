from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for i in words:
            waiting[i[0]].append(i)
        total = len(words)
        for i in S:
            h = waiting[i]
            waiting[i] = []
            for g in h:
                if len(g) > 1:
                    waiting[g[1]].append(g[1:])
            #print(waiting)
        for i,j in waiting.items():
            total -= len(j)
        return total
