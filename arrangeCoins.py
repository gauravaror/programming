class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        sum_ = 0 
        while True:
            if sum_ + i <= n:
                sum_ += i
                i+=1
            else:
                return i - 1
