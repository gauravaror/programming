class Solution:
    def makeGood(self, s: str) -> str:
        def back(s, i):
            if i >= len(s):
                return s
            if i + 1 < len(s):
                #print(s, i)
                first = ord(s[i])
                second = ord(s[i+1])
                if abs(first-second) == 32:
                    initial = s[:i]
                    after = s[i+2:] if i+2 < len(s) else ''
                    g = initial + after
                    ind = i-1 if i-1>=0  else 0
                    return back(g, ind)
            return back(s, i+1)
        return back(s, 0)
