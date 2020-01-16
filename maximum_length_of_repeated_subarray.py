class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        tracker = [[0]*len(B) for _ in A]
        max_l = 0
        for idx,i in enumerate(A):
            for jdx,j in enumerate(B):
                if A[idx] == B[jdx]:
                    if idx >= 1 and jdx >= 1:
                        tracker[idx][jdx] = tracker[idx-1][jdx-1] + 1
                    else:
                        tracker[idx][jdx] = 1
                    if tracker[idx][jdx] > max_l:
                        max_l = tracker[idx][jdx]
        return max_l
