class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        acc = 0
        d = [0]*K
        d[0] = 1
        for i in range(len(A)):
            acc += A[i]
            d[acc % K] += 1
        print(d)
        return int(sum([ i*(i-1)/2 for i in d]))
