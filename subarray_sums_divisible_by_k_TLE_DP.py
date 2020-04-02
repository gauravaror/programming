class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dp = [[0]*len(A) for _ in range(len(A))]
        dividk = 0
        for idx,i in enumerate(A):
            dp[idx][idx] = i
            if dp[idx][idx] % K == 0:
                dividk += 1
  #              print(idx,idx)

        for start_idx in range(len(A)):
            for length in range(1, len(A)-start_idx):
                if start_idx + length < len(A):
                    dp[start_idx][start_idx +length] = dp[start_idx][start_idx + length-1] + A[start_idx+length]
                    if dp[start_idx][start_idx +length] % K == 0:
                        dividk += 1
 #                       print(start_idx, start_idx+length, dp[start_idx][start_idx +length])
#        print(dp)
        return dividk
