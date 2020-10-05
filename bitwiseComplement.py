class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        m = 1
        ans = 0
        first_non = False
        for i in range(31,-1,-1):
            bit = 1 if (N&(1<<i)) == 0 else 0
            if bit == 0:
                first_non = True
            if not first_non:
                continue
            ans = ans*2 + bit
            #print(i, bit, ans, pow(2,i))
        return ans 
