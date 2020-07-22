class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        iw2 = iw3 = iw5 = 0
        last = 1
        
        while len(ugly) < n:
            while (ugly[iw2]*2 <= last):
                iw2 += 1
            while (ugly[iw3]*3 <= last):
                iw3 += 1
            while (ugly[iw5]*5 <= last):
                iw5 += 1
            last = min(ugly[iw2]*2, ugly[iw3]*3, ugly[iw5]*5)
            #iw2 = iw3 = iw5 = last
            #print(iw2, iw3, iw5, last, ugly)
            ugly.append(last)
        return ugly[-1]
