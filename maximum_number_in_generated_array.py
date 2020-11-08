class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 1:
            return 0
        arr = [0]*(n+1)
        arr[1] = 1
        for i in range(2, n+1):
            a = i//2
            if i%2 == 0:
                arr[i] = arr[a]
            else:
                arr[i] = arr[a] + arr[a+1]
        return max(arr)
        
        
