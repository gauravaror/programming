class Solution:
    def minOperations(self, nums: List[int]) -> int:
        self.cache = {}
        def ops(n):
            twos = 0
            ones = 0
            num = n
            while n > 0:
                if n in self.cache:
                    o,t = self.cache[n]
                    ones += o
                    twos += t
                    break
                if n % 2 == 0:
                    n = n //2
                    twos += 1
                else:
                    n = n - 1
                    ones += 1
            self.cache[num] = (ones,twos)
            return (ones, twos)
        final_twos = 0
        final_ones = 0
        for i in nums:
            o,t  = ops(i)
            final_ones += o
            final_twos = max(final_twos, t)
        return final_ones + final_twos

