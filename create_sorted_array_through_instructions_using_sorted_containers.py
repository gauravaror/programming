from sortedcontainers import SortedList
class Solution:

    def createSortedArray(self, instructions: List[int]) -> int:
        #print("ins", instructions)
        sl = SortedList()
        ma = max(instructions)
        c = Counter()
        cost = 0
        for idx,i in enumerate(instructions):
            less = sl.bisect_left(i)
            equal = c[i]
            #print("Less Equal", less, equal, cost)
            cost += min(less, idx-less-equal)
            sl.add(i)
            c[i] += 1
        return cost % (10**9 + 7)


