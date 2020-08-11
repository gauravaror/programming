from collections import Counter
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        maxcite = max(citations)
        c = Counter()
        c.update(citations)
        cumpapers = 0
        print
        for i in range(1, maxcite+1)[::-1]:
            cumpapers += c[i]
            if cumpapers >= i:
                return i
        return 0
