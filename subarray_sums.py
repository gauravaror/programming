class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = defaultdict(list)
        dp[0].append(-1)
        cumsum = 0
        arrs = 0
        for i in nums:
            cumsum += i
            if cumsum-k in dp:
                arrs += len(dp[cumsum-k])
            dp[cumsum].append(i)
        return arrs
