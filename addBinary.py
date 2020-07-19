class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rb = b[::-1]
        ra = a[::-1]
        reminder = 0
        output = ""
        lena = len(a)
        lenb = len(b)
        lenmin = min(lena, lenb)
        lenmax = max(lena, lenb)
        ma = ra if lena > lenb else rb
        for i in range(lenmin):
            s = int(ra[i]) + int(rb[i]) + reminder
            print(i,s, output)
            if s == 3:
                output += str(1)
                reminder = 1
            elif s == 2:
                output += str(0)
                reminder = 1
            elif s == 1:
                output += str(1)
                reminder = 0
            elif s == 0:
                output += "0"
            
        for i in range(lenmin, lenmax):
            now = int(ma[i]) + reminder
            if now == 2:
                reminder = 1
                output += str(0)
            else:
                output += str(now)
                reminder = 0
        if reminder == 1:
            output += "1"
        return output[::-1]
