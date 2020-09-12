class Solution:
    def backtrack(self, A, B, a,b, index, swaps):
        if index > len(A)-1:
            self.mina = min(self.mina, swaps)
            return
        if (a,b,index,swaps) in self.dp:
            return 
        self.dp.add((a,b,index,swaps))
        if index == 0 or (A[index] > a and B[index] > b):
            self.backtrack(A, B, A[index], B[index], index+1, swaps)
        if index == 0 or (B[index] > a and A[index] > b):
           # A[index], B[index] = B[index], A[index]
            self.backtrack(A, B, B[index], A[index], index+1, swaps+1)
            #A[index], B[index] = B[index], A[index]
        
            
        
    def minSwap(self, A: List[int], B: List[int]) -> int:
        self.mina = float('inf')
        self.dp = set()
        self.backtrack(A, B, 0, 0, 0, 0)
        return self.mina
