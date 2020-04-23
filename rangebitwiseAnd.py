class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        if m == n:
            return m
        two_powers = 0
        starts_at = False
        for i in range(1, 31):
            this_one = pow(2,i)
            if m == this_one:
                starts_at = True
            if this_one >= m and this_one <= n:
                two_powers += 1
        print(two_powers)
        if two_powers > 0 and not (starts_at and two_powers==1):
            return 0
        bit_and = m
        print(bin(bit_and))
        i = m+1                
        while i <= n:
            bit_and &= i
            inc = 1
            i += inc
            if bit_and == 0:
                break
        return bit_and
