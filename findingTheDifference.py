class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        smap = defaultdict(int)
        output = ''
        for i in s:
            smap[i] += 1
        for i in t:
            if smap[i] > 0:
                smap[i] -= 1
            else:
                output += i
        return output
