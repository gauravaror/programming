class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        print(c)
        out = []
        for i  in c.keys():
            if c[i] > 1:
                continue
            elif c[i-1] == 0 and c[i+1] == 0:
                out.append(i)
        return out
