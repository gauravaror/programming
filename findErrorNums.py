class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n*(n+1)//2
        ts = sum(nums)
        eqn = ts-s
        hs = set()
        dup = -1
        for i in nums:
            if i in hs:
                dup = i
                break
            hs.add(i)
        return [dup, dup-eqn]
