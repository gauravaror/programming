import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        wlen = len(s1)
        def compare(c, d):
            for i in string.ascii_lowercase:
                if c[i] != d[i]:
                    return False
            return True
        c = defaultdict(lambda: 0)
        d = defaultdict(lambda: 0)
        ans = []
        for i in s1:
            c[i] += 1
        for i in range(len(s2)-wlen+1):
            if i == 0:
                for j in range(wlen):
                    d[s2[j]] += 1
            else:
                d[s2[i-1]] -= 1
                d[s2[i+wlen-1]] += 1
            #print(i, c, d)
            if compare(c,d):
                ans.append(i)   
        return len(ans) > 0
