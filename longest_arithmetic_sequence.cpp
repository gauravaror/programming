class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        length = len(A)
        dp = {}
        print(length)
        for i in range(length):
            dp[(i,A[i] - A[0])] = 1
        max_sequence = 1
        for i in range(1, length):
            for j in range (i+1, length):
                current = A[j] - A[i]
                current_seq = 1
                if (i, current) in dp:
                    dp[(j, current)] = dp[(i,current)] + 1
                else:
                    dp[(j,current)]  = 1
                if dp[(j,current)] > max_sequence:
                    max_sequence  = dp[(j,current)]
        return max_sequence+1
