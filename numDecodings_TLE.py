class Solution:
    def numDecodings(self, s: str) -> int:
        self.ans = 0
        def back(st):
            if len(st) == 0:
                self.ans += 1
                return
            if st[0] != "0":
                back(st[1:])
            #print(st[:2])
            if len(st) >= 2 and int(st[:2]) <= 26 and st[0] != "0":
                back(st[2:])
        back(s)
        return self.ans
