class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]
        dp = {0: A[0]}
        lst = 0
        acc = 0
        max_sub = -float('inf')
        for ind in range(1, 2*len(A)):
            if max(0, dp[ind-1]) == 0:
                lst = ind
            dp[ind] = max(0,dp[ind-1]) + A[ind%len(A)]
            #print(ind, lst, ind-len(A)+1)
            if lst < ind-len(A)+1:
                removed = 0
                #print(ind, lst, ind-len(A)+1)
                for de in range(lst, ind-len(A)+1):
                    dp[ind] -= A[de%len(A)]
                    removed += A[de%len(A)]
                lst = ind-len(A)+1
                reset_index = lst
                removed1 = 0
                rm = 0
                for ge in range(ind-len(A)+1, ind):
                    removed1 += A[ge%len(A)]
                    #print("loo", removed1, ge, lst)
                    if removed1 < rm:
                        reset_index = ge + 1
                        rm = removed1
                    if removed1 >= 0:
                        dp[ind] -= rm
                        lst = reset_index
                        break
                #print("end", ind, lst, ind-len(A)+1)
                #dp[ind + 1] -= rm
                #lst = reset_index + 1
            #else:
            #    lst = ind
            #    dp[ind+1] = A[ind%len(A)]
        #print(dp)
        return max(dp.values())
