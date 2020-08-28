class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        bestL = [0]*len(A)
        bestM = [0]*len(A)
        curr = 0
        Lsum = 0
        Msum = 0
        ans = 0
        for idx,i in enumerate(A):
            curr += 1
            Lsum += i
            Msum += i
            if curr >= L:
                if curr > L:
                    Lsum -= A[idx-L]
                bestL[idx] = max(bestL[idx-1], Lsum)
            if curr >= M:
                if curr > M:
                    Msum -= A[idx-M]
                bestM[idx] = max(bestM[idx-1], Msum)
            
            ans = max(Msum + bestL[idx-M], Lsum + bestM[idx-L], ans)
        print(bestL, bestM)
        return ans
