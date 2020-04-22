from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        acc = 0
        dp = defaultdict(list)
        su = defaultdict(lambda: 0)
        for i in range(len(nums)):
            acc += nums[i]
            dp[acc].append(i)
            su[i] = acc
        #print(dp, su)
        for i in range(len(nums)):
            before = su[i] - k
            if su[i] == k:
                output += 1
            if before in dp:
                for d in dp[before]:
                    if d < i:
                        #print("Before", i, su[i], d, su[d], before, k)
                        output += 1
        return output
