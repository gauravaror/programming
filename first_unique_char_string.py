from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter()
        c.update(s)
        print(c)
        for idx,i in enumerate(s):
            if c[i] == 1:
                return idx
        return -1
