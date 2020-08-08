class Solution:
    def maxArea(self, height: List[int]) -> int:
        ma = 0
        for sidx, start in enumerate(height):
            for eidx, end in enumerate(height):
                diff = abs(sidx-eidx)
                mheight = min(start, end)
                ma = max(ma, diff*mheight)
        return ma
