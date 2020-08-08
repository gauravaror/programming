class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        ma = 0
        while start < end:
            diff = abs(end-start)
            mheight = min(height[start], height[end])
            ma = max(ma, diff*mheight)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return ma
