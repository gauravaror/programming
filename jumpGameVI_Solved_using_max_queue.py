from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [-float('inf')]*len(nums)
        dp[len(nums)-1] = nums[-1]
        qu = deque()
        qu.append([nums[-1], len(nums)-1])
        for i in range(len(nums)-2, -1, -1):
            dp[i] = nums[i] + qu[0][0]
            while qu and dp[i] > qu[-1][0]:
                qu.pop()
            qu.append([dp[i],i])
            while qu[0][1] >= i+k:
                qu.popleft()
        return dp[0]
