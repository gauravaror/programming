class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        min_length = len(A) + 10
        start = 0
        end = 0
        currsum = 0
        while start < len(A):
            if currsum < K and  end < len(A):
                currsum += A[end]
                end += 1
            elif currsum >= K:
                if currsum >= K:
                    min_length = min(min_length, end-start)
                currsum -= A[start]
                start += 1
            else:
                currsum -= A[start]
                start += 1
        if min_length == len(A) + 10:
            return -1
        return min_length
