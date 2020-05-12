class Solution:
    def trap(self, height: List[int]) -> int:
        dpf = [-1]*len(height)
        dpb = [-1]*len(height)
        prev = -1
        for idx,i in enumerate(height):
            if i > prev:
                prev = i
            dpf[idx] = prev
        prev = -1
        for idx,i in enumerate(height[::-1]):
            if i > prev:
                prev = i
            dpb[len(height)-1-idx] = prev
        ans = 0
        for h,f,b in zip(height,dpf,dpb):
            m = min(f,b)
            if m - h > 0:
                ans += (m-h)
        return ans
