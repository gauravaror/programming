class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(0,10))
        self.output = []
        def make_number(dig):
            n = 0
            num = 0
            for i in dig[::-1]:
                num += i*pow(10,n)
                n += 1
            return num
                
        def back(curr):
            if len(curr) == N:
                self.output.append(make_number(curr))
                return
            if len(curr) == 0:
                for i in range(1, 10):
                    back([i])
            else:
                last_dig = curr[-1]
                if last_dig - K >= 0:
                    back(curr + [last_dig-K])
                
                if K != 0 and last_dig + K <= 9:
                    back(curr + [last_dig+K])
        back([])
        return self.output
