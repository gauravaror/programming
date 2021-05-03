class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if ans:
                ans.append(i+ ans[-1])
            else:
                ans.append(i)
        return ans
