from collections import Counter,defaultdict
import string
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        wlen = len(p)
        def compare(c, d):
            for i in string.ascii_lowercase:
                if c[i] != d[i]:
                    return False
            return True
        c = defaultdict(lambda: 0)
        d = defaultdict(lambda: 0)
        ans = []
        for i in p:
            c[i] += 1
        for i in range(len(s)-wlen+1):
            if i == 0:
                for j in range(wlen):
                    d[s[j]] += 1
            else:
                d[s[i-1]] -= 1
                d[s[i+wlen-1]] += 1
            #print(i, c, d)
            if compare(c,d):
                ans.append(i)   
        return ans
