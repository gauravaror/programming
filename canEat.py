class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        for c in range(1, len(candiesCount)):
            candiesCount[c] += candiesCount[c-1]
        output = []
        for typ, day, cap in queries:
            if (day+1)*cap  <= candiesCount[typ-1] and typ != 0:
                output.append(False)
                continue
            if day+1 > candiesCount[typ]:
                output.append(False)
                continue
            output.append(True)
        return output
