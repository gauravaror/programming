import sortedcontainers
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sl = sortedcontainers.SortedList()
        for i in nums:
            sl.add(i)
        output = []
        for i in queries:
            check = i[0]
            ind = sl.bisect_right(i[1])
            maxa = -1
            for j in range(ind):
                maxa = max(maxa, sl[j] ^ check)
            output.append(maxa)
        return output
