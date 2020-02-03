class Solution:
    
    def do_operations(self, N, neg=False):
        if N >= 5:
            ans=(N*(N-1) // (N-2)) 
            if neg:
                ans = ans*-1
            ans = ans + (N-3) + self.do_operations(N-4, True)
        elif N==4:
            ans = (N*(N-1) // (N-2))
            if neg:
                ans = ans*-1
            ans =  ans + (N-3)
        elif N==3:
            ans = (N*(N-1) // (N-2))
            if neg:
                ans = ans*-1
        elif N==2:
            ans = (N*(N-1))
            if neg:
                ans  = ans*-1
        else:
            ans = N
            if neg:
                ans  = ans*-1
        print(N, ans)
        return ans
            
            
    def clumsy(self, N: int) -> int:
        print("Doing ", N)
        return self.do_operations(N)
