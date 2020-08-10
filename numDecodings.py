class Solution:
    def numDecodings(self, s: str) -> int:
        self.ans = 0
        self.cache = {}
        def back(st):
            if len(st) == 0:
                self.ans += 1
                self.cache[st] = 1
                return 1
            ans = 0
            if st[0] != "0":
                if st[1:] not in self.cache:
                    g = back(st[1:])
                    ans += g
                else:
                    if self.cache[st[1:]]:
                        ans += self.cache[st[1:]]
            #print(st[:2])
            if len(st) >= 2 and int(st[:2]) <= 26 and st[0] != "0":
                if st[2:] not in self.cache:
                    l = back(st[2:])
                    ans += l
                else:
                    if self.cache[st[2:]]:
                        ans += self.cache[st[2:]]
            self.cache[st] = ans
            return ans
        return back(s)
