class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        c = Counter()
        for i in range(lowLimit, highLimit+1):
            num = i
            su = 0
            while num:
                num, rem = divmod(num, 10)
                su += rem
            c[su] += 1
        return c.most_common()[0][1]
                
                
        
