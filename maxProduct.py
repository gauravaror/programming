class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cum = 1
        maxa = nums[0]
        mina = nums[0]
        res = nums[0]
        for n in nums[1:]:
            maxa, mina = max(maxa*n, mina*n, n), min(maxa*n, mina*n, n)
            res = max(maxa, res)
            print(res, maxa, mina, n)
        return res
