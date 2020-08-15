class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        end = 0
        num_zeros = 0
        max_len = 0
        while end < len(A):
            if num_zeros <= K:
                max_len = max(max_len, end-start)
            if num_zeros > K:
                if A[start] == 0:
                    num_zeros -= 1
                start += 1
            else:
                if A[end] == 0:
                    num_zeros += 1
                end += 1
        if num_zeros <= K:
            max_len = max(max_len, end-start)
        return max_len
