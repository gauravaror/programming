class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start = 0
        end = 0
        while end < len(A):
            if A[end] % 2 == 0:
                A[start], A[end] = A[end],A[start]
                start += 1
                end += 1
            else:
                end += 1
        return A
