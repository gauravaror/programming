class NumArray:

    def __init__(self, nums: List[int]):
        self.cum = [0]
        for idx,i in enumerate(nums):
            prev = self.cum[-1]
            self.cum.append(prev + i)
        print(self.cum)

    def sumRange(self, i: int, j: int) -> int:
        mina = self.cum[i]
        return self.cum[j+1] - mina
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
