class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        c1 = Counter([ x+y for x,y in itertools.product(A,B)])
        c2 = Counter([ x+y for x,y in itertools.product(C,D)])
        output = 0
        for i,j in c1.items():
            if -i in c2:
                output += j*c2[-i]
        return output
