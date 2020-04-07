class Solution:
    def countElements(self, arr: List[int]) -> int:
        hh = {}
        for i in arr:
            hh[i] = 1
        count = 0
        for i in arr:
            if i+1 in hh:
                count += 1
        return count
