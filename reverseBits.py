class Solution:
    def reverseBits(self, n: int) -> int:
        st = 1
        num = 32
        output = 0
        while num >= 0:
            num -= 1
            bit = n&st
            if bit:
                output += pow(2,num)
            st = st << 1
            #print(st, num, output)
        return output
