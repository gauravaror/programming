class Solution:
    def countElements(self, nums: List[int]) -> int:
        c = Counter()
        total = len(nums)
        c.update(nums)
        maxa = max(nums)
        mina = min(nums)
        if mina ==  maxa:
            return 0
        return total - c[maxa] -  c[mina]
