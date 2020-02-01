class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        length = len(A)
        dp = [[(0,0) for _ in A] for _ in A]
        print(length)
        for i in range(length):
            dp[0][i] = (A[i] - A[0],1)
        max_sequence = 1
        max_sequence_start = (0,0)
        for i in range(1, length):
            for j in range (i+1, length):
                current = A[j] - A[i]
                current_seq = 1
                for k in range(0,j):
                    #print(current,dp[k][i])
                    if current  == dp[k][i][0]:
                        if dp[k][i][1]+1 > current_seq:
                            current_seq = dp[k][i][1] + 1 
                #print("current_seq")
                dp[i][j] = (current, current_seq)
                if current_seq > max_sequence:
                    max_sequence  = current_seq
                    max_sequence_start = (i,j)
        #print(max_sequence, max_sequence_start)
        #print(dp)
        return max_sequence+1
