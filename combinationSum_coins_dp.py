from collections import defaultdict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = defaultdict(list)
        dp[0].append([])
        for j in candidates:
            for i in range(target+1):
                if i-j in dp:
                    for elem in dp[i-j]:
                        elem1 = elem.copy()
                        elem1.append(j)
                        dp[i].append(elem1)
        print(dp)
        if target in dp:
            return dp[target]
        else:
            return []
