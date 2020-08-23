class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -1
        dp = {}
        mgroup = 0
        for idx,i in enumerate(arr):
            lo = arr[idx]
            hi = arr[idx]
            dp[lo] = 1
            while lo -1  > 0 and lo -1 in dp:
                lo -= dp[lo-1]
            while hi + 1 <= len(arr) and hi +1 in dp:
                hi += dp[hi+1]
            le = hi - lo + 1
            if le == m:
                mgroup += 1
            g = arr[idx]
            if g-1 > 0 and g-1 in dp and dp[g-1] == m:
                mgroup -= 1
            if g+1 <= len(arr) and g+1 in dp and dp[g+1] == m:
                mgroup -= 1
            dp[lo] = le
            dp[hi] = le
            if mgroup > 0:
                res = idx + 1
            #print(dp, mgroup)
        return res
